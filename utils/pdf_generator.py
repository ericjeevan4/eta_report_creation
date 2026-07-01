from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def add_llm_section(
    story,
    styles,
    title,
    stats_text,
    inference,
    conclusion
):

    story.append(
        Paragraph(
            title,
            styles["Heading1"]
        )
    )

    story.append(
        Paragraph(
            stats_text,
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 10)
    )

    story.append(
        Paragraph(
            "Inference",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            inference,
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 10)
    )

    story.append(
        Paragraph(
            "Conclusion",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            conclusion,
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 20)
    )


def generate_pdf(
    report_data,
    llm_sections,
    output_path
):

    doc = SimpleDocTemplate(output_path)

    styles = getSampleStyleSheet()

    story = []


    # =====================================================
    # TITLE
    # =====================================================

    story.append(
        Paragraph(
            "Detailed Analysis Report",
            styles["Title"]
        )
    )

    story.append(
        Spacer(1, 20)
    )


    # =====================================================
    # DATASET OVERVIEW
    # =====================================================

    story.append(
        Paragraph(
            "1. Dataset Overview",
            styles["Heading1"]
        )
    )

    dataset_text = f"""
    Total Observations:
    <b>{report_data['dataset']['total_rows']}</b>
    <br/><br/>

    Total Variables:
    <b>{report_data['dataset']['total_columns']}</b>
    """

    story.append(
        Paragraph(
            dataset_text,
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 20)
    )


    # =====================================================
    # LEVEL 0
    # =====================================================

    level0_stats = f"""
    Pass Count:
    <b>{report_data['level0']['pass_count']}</b>
    <br/>

    Hold Count:
    <b>{report_data['level0']['hold_count']}</b>
    <br/>

    Pass Percentage:
    <b>{report_data['level0']['pass_percentage']}%</b>
    """

    add_llm_section(
        story,
        styles,
        "2. Level-0 Operation",
        level0_stats,
        llm_sections["level0"]["inference"],
        llm_sections["level0"]["conclusion"]
    )


    # =====================================================
    # LEVEL 1
    # =====================================================

    level1_stats = f"""
    Hold Count:
    <b>{report_data['level1']['hold_count']}</b>
    <br/>

    Go To Level 2:
    <b>{report_data['level1']['go_to_level2_count']}</b>
    <br/>

    Hold Percentage:
    <b>{report_data['level1']['hold_percentage']}%</b>
    <br/>

    Level 2 Percentage:
    <b>{report_data['level1']['level2_percentage']}%</b>
    """

    add_llm_section(
        story,
        styles,
        "3. Level-1 Behaviour",
        level1_stats,
        llm_sections["level1"]["inference"],
        llm_sections["level1"]["conclusion"]
    )


    # =====================================================
    # LEVEL 2
    # =====================================================

    level2_stats = f"""
    Raise Count:
    <b>{report_data['level2']['raise_count']}</b>
    <br/>

    Hold Count:
    <b>{report_data['level2']['hold_count']}</b>
    <br/>

    Evaluation Percentage:
    <b>{report_data['level2']['evaluation_percentage']}%</b>
    """

    add_llm_section(
        story,
        styles,
        "4. Level-2 Behaviour",
        level2_stats,
        llm_sections["level2"]["inference"],
        llm_sections["level2"]["conclusion"]
    )


    # =====================================================
    # CHILLER 1
    # =====================================================

    ch1_stats = f"""
    Hold Percentage:
    <b>{report_data['ch1']['hold_percentage']}%</b>
    <br/>

    Raise Percentage:
    <b>{report_data['ch1']['raise_percentage']}%</b>
    <br/>

    Reduce Percentage:
    <b>{report_data['ch1']['reduce_percentage']}%</b>
    """

    add_llm_section(
        story,
        styles,
        "5. Chiller 1 Analysis",
        ch1_stats,
        llm_sections["ch1"]["inference"],
        llm_sections["ch1"]["conclusion"]
    )


    # =====================================================
    # CHILLER 2
    # =====================================================

    ch2_stats = f"""
    Hold Percentage:
    <b>{report_data['ch2']['hold_percentage']}%</b>
    <br/>

    Raise Percentage:
    <b>{report_data['ch2']['raise_percentage']}%</b>
    <br/>

    Reduce Percentage:
    <b>{report_data['ch2']['reduce_percentage']}%</b>
    """

    add_llm_section(
        story,
        styles,
        "6. Chiller 2 Analysis",
        ch2_stats,
        llm_sections["ch2"]["inference"],
        llm_sections["ch2"]["conclusion"]
    )


    # =====================================================
    # COMPARISON
    # =====================================================

    comparison_stats = f"""
    CH1 Hold:
    <b>{report_data['comparison']['ch1_hold']}</b>
    <br/>

    CH2 Hold:
    <b>{report_data['comparison']['ch2_hold']}</b>
    <br/>

    CH1 Raise:
    <b>{report_data['comparison']['ch1_raise']}</b>
    <br/>

    CH2 Raise:
    <b>{report_data['comparison']['ch2_raise']}</b>
    """

    add_llm_section(
        story,
        styles,
        "7. Chiller Comparison",
        comparison_stats,
        llm_sections["comparison"]["inference"],
        llm_sections["comparison"]["conclusion"]
    )

    story.append(
        Paragraph(
            "8. Chiller 1 Current Operating Setpoint",
            styles["Heading1"]
        )
    )

    story.append(
        Paragraph(
            f"""
            Mean:
            <b>{report_data['ch1_current']['mean']}°C</b><br/>

            Median:
            <b>{report_data['ch1_current']['median']}°C</b><br/>

            Min:
            <b>{report_data['ch1_current']['min']}°C</b><br/>

            Max:
            <b>{report_data['ch1_current']['max']}°C</b>
            """,
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            llm_sections["ch1_current"]["inference"],
            styles["BodyText"]
        )
    )

    ###

    story.append(
        Paragraph(
            "9. Chiller 1 Recommended Setpoint",
            styles["Heading1"]
        )
    )

    story.append(
        Paragraph(
            f"""
            Mean:
            <b>{report_data['ch1_recommended']['mean']}°C</b><br/>

            Median:
            <b>{report_data['ch1_recommended']['median']}°C</b><br/>

            Min:
            <b>{report_data['ch1_recommended']['min']}°C</b><br/>

            Max:
            <b>{report_data['ch1_recommended']['max']}°C</b>
            """,
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            llm_sections["ch1_recommended"]["inference"],
            styles["BodyText"]
        )
    )

    ###

    story.append(
        Paragraph(
            "10. Chiller 2 Current Operating Setpoint",
            styles["Heading1"]
        )
    )

    story.append(
        Paragraph(
            f"""
            Mean:
            <b>{report_data['ch2_current']['mean']}°C</b><br/>

            Median:
            <b>{report_data['ch2_current']['median']}°C</b><br/>

            Min:
            <b>{report_data['ch2_current']['min']}°C</b><br/>

            Max:
            <b>{report_data['ch2_current']['max']}°C</b>
            """,
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            llm_sections["ch2_current"]["inference"],
            styles["BodyText"]
        )
    )

    ###

    story.append(
        Paragraph(
            "11. Chiller 2 Recommended Setpoint",
            styles["Heading1"]
        )
    )

    story.append(
        Paragraph(
            f"""
            Mean:
            <b>{report_data['ch2_recommended']['mean']}°C</b><br/>

            Median:
            <b>{report_data['ch2_recommended']['median']}°C</b><br/>

            Min:
            <b>{report_data['ch2_recommended']['min']}°C</b><br/>

            Max:
            <b>{report_data['ch2_recommended']['max']}°C</b>
            """,
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            llm_sections["ch2_recommended"]["inference"],
            styles["BodyText"]
        )
    )

    ###

    story.append(
        Paragraph(
            "12. Key Difference Between the Two Chillers",
            styles["Heading1"]
        )
    )

    story.append(
        Paragraph(
            llm_sections["comparison_takeaway"]["inference"],
            styles["BodyText"]
        )
    )

    ###

    story.append(
        Paragraph(
            "13. Setpoint Reduction Opportunities are Extremely Rare",
            styles["Heading1"]
        )
    )

    story.append(
        Paragraph(
            f"""
            Chiller 1 Reduce Count:
            <b>{report_data['rare_reduction']['ch1_reduce']}</b><br/>

            Chiller 2 Reduce Count:
            <b>{report_data['rare_reduction']['ch2_reduce']}</b>
            """,
            styles["BodyText"]
        )
    )

    ###

    story.append(
        Paragraph(
            "14. Hierarchical Decision Structure",
            styles["Heading1"]
        )
    )

    story.append(
        Paragraph(
            f"""
            {report_data['hierarchy']['total_rows']} observations<br/>
            ↓<br/>
            Level-0<br/>
            ↓<br/>
            {report_data['hierarchy']['level0_pass']} pass<br/>
            ↓<br/>
            Level-1<br/>
            ↓<br/>
            {report_data['hierarchy']['level1_hold']} hold<br/>
            {report_data['hierarchy']['level2_count']} → Level-2<br/>
            ↓<br/>
            {report_data['hierarchy']['level2_raise']} raise setpoint<br/>
            {report_data['hierarchy']['level2_hold']} hold
            """,
            styles["BodyText"]
        )
    )

    ###

    story.append(
        Paragraph(
            "Overall Interpretation",
            styles["Heading1"]
        )
    )

    story.append(
        Paragraph(
            llm_sections["overall_takeaway"]["inference"],
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    story.append(
        Paragraph(
            "Overall Plant Behaviour",
            styles["Heading1"]
        )
    )

    story.append(
        Paragraph(
            llm_sections["comparison_takeaway"]["inference"],
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    story.append(
        Paragraph(
            "Main Takeaway",
            styles["Heading1"]
        )
    )

    story.append(
        Paragraph(
            llm_sections["main_takeaway"]["inference"],
            styles["BodyText"]
        )
    )

    ###


    doc.build(story)

    print(f"PDF generated: {output_path}")