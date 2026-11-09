
import streamlit as st

# =====================================
# 1. PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Grade Manager")
st.write("Add students and manage their academic performance.")

st.divider()


# =====================================
# 2. GRADING SCALE
# =====================================

def get_grade(mark):

    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


# =====================================
# 3. SESSION STATE
# =====================================

if "students" not in st.session_state:
    st.session_state.students = []


# =====================================
# 4. ADD STUDENT FORM
# =====================================

st.subheader("Add New Student")

with st.form("add"):

    name = st.text_input(
        "Name",
        placeholder="Enter student name"
    )

    mark = st.number_input(
        "Mark",
        min_value=0,
        max_value=100,
        value=0,
        step=1
    )

    submitted = st.form_submit_button("Add")

    if submitted:

        if not name.strip():

            st.error("Please enter a student name.")

        elif mark < 0 or mark > 100:

            st.error("Invalid mark! Enter a mark between 0 and 100.")

        else:

            student = {
                "Name": name.strip(),
                "Mark": mark,
                "Grade": get_grade(mark)
            }

            st.session_state.students.append(student)

            st.success(f"{name.strip()} added successfully!")


st.divider()


# =====================================
# 5. DISPLAY STUDENT TABLE
# =====================================

st.subheader("Student Results")

if st.session_state.students:

    st.table(st.session_state.students)

    # =================================
    # 6. CALCULATE CLASS STATISTICS
    # =================================

    marks = [
        student["Mark"]
        for student in st.session_state.students
    ]

    average = sum(marks) / len(marks)

    highest = max(marks)

    lowest = min(marks)

    # =================================
    # 7. DISPLAY CLASS METRICS
    # =================================

    st.subheader("Class Performance")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Class Average",
            value=f"{average:.2f}"
        )

    with col2:
        st.metric(
            label="Highest Mark",
            value=highest
        )

    with col3:
        st.metric(
            label="Lowest Mark",
            value=lowest
        )

else:

    st.info("No students added yet. Please add a student.")


st.divider()


# =====================================
# 8. GRADING SCALE REFERENCE
# =====================================

st.subheader("Grading Scale")

st.table({
    "Mark Range": [
        "90 - 100",
        "80 - 89",
        "70 - 79",
        "60 - 69",
        "Below 60"
    ],
    "Grade": [
        "A",
        "B",
        "C",
        "D",
        "E"
    ]
})


# =====================================
# 9. FOOTER
# =====================================

st.caption("Week 1 | Day 4 Assignment - Student Grade Manager")
