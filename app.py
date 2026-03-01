import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Employee Analytics Dashboard",
    layout="wide",
)

def generate_employee_data(num_employees: int = 10): # pd.DataFrame:
    np.random.seed(42)

    first_names = [
        "Alex", "Jordan", "Taylor", "Morgan", "Casey", "Riley", "Jamie",
        "Cameron", "Drew", "Avery"
    ]
    last_names = [
        "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia",
        "Miller", "Davis", "Rodriguez", "Martinez"
    ]

    names = [
        f"{np.random.choice(first_names)} {np.random.choice(last_names)}"
        for _ in range(num_employees)
    ]

    df = pd.DataFrame({
        "Name": names,
        "Salary": np.random.randint(40000, 150001, size=num_employees),
        "Experience (Years)": np.random.randint(0, 31, size=num_employees),
        "Performance Rating": np.random.choice(
            ["Excellent", "Good", "Average", "Below Average"],
            size=num_employees,
            p=[0.25, 0.40, 0.25, 0.10]
        )
    })
    return df

def main():
    st.title("Employee Performance Analysis")
    st.markdown("Interactive dashboard to analyze **employee salary, experience, and performance**.")

    st.sidebar.header("Dashboard Controls")
    chart_option = st.sidebar.radio(
        "Select Visualization",
        [
            "Employee Dataset",
            "Salary by Employee (Bar Chart)",
            "Performance Distribution (Pie Chart)",
            "Experience vs Salary (Line Chart)",
            "Experience vs Salary (Scatter Plot)"
        ]
    )

    df = generate_employee_data(10)

    if chart_option == "Employee Dataset":
        st.subheader("Employee Dataset")
        st.dataframe(df, use_container_width=True)

    elif chart_option == "Salary by Employee (Bar Chart)":
        st.subheader("Salary by Employee")
        df_sorted = df.sort_values("Salary", ascending=False)
        fig, ax = plt.subplots(figsize=(6, 2))
        sns.barplot(x="Name", y="Salary", data=df_sorted, ax=ax,palette="Blues_r")
        ax.set_xlabel("Employee Name", fontsize=10)
        ax.set_ylabel("Salary", fontsize=10)
        ax.tick_params(axis='x', labelsize=8, rotation=45)
        ax.tick_params(axis='y', labelsize=8)
        st.pyplot(fig)

    elif chart_option == "Performance Distribution (Pie Chart)":
        st.subheader("Performance Rating Distribution")
        rating_counts = df["Performance Rating"].value_counts()
        fig, ax = plt.subplots(figsize=(3, 3))
        ax.pie(rating_counts.values, labels=rating_counts.index, autopct="%1.1f%%",startangle=90)
        ax.axis("equal")
        st.pyplot(fig)

    elif chart_option == "Experience vs Salary (Line Chart)":
        st.subheader("Experience vs Salary")
        df_sorted = df.sort_values("Experience (Years)")
        fig, ax = plt.subplots(figsize=(7, 3))
        sns.lineplot(x="Experience (Years)", y="Salary", data=df_sorted, marker="o", ax=ax)
        ax.set_xlabel("Experience (Years)")
        ax.set_ylabel("Salary (USD)")
        st.pyplot(fig)

    elif chart_option == "Experience vs Salary (Scatter Plot)":
        st.subheader("Experience vs Salary (Scatter Plot)")
        fig, ax = plt.subplots(figsize=(7, 3))
        sns.scatterplot(x="Experience (Years)", y="Salary", hue="Performance Rating", data=df, ax=ax, s=80)
        ax.set_xlabel("Experience (Years)")
        ax.set_ylabel("Salary")
        st.pyplot(fig)

if __name__ == "__main__":
    main()