import pandas as pd

from utils.analyzer import analyze_csv
from utils.pdf_generator import generate_pdf

from utils.llm_generator import (
generate_level0_inference,
generate_level0_conclusion,
generate_level1_inference,
generate_level1_conclusion,
generate_level2_inference,
generate_level2_conclusion,
generate_ch1_inference,
generate_ch1_conclusion,
generate_ch2_inference,
generate_ch2_conclusion,
generate_comparison_inference,
generate_comparison_conclusion,
generate_main_takeaway,
generate_ch1_current_inference,
generate_ch1_recommended_inference,
generate_ch2_current_inference,
generate_ch2_recommended_inference,
generate_comparison_takeaway,
generate_overall_takeaway
)

# =====================================================

# LOAD CSV

# =====================================================

df = pd.read_csv("data/recommendations.csv")

# =====================================================

# ANALYZE CSV

# =====================================================

report_data = analyze_csv(df)

# =====================================================

# LEVEL 0

# =====================================================

level0_inference = generate_level0_inference(
report_data["dataset"]["total_rows"],
report_data["level0"]["pass_count"],
report_data["level0"]["hold_count"]
)

level0_conclusion = generate_level0_conclusion(
    report_data["level0"]["pass_count"],
    report_data["level0"]["hold_count"]
)

# =====================================================

# LEVEL 1

# =====================================================

level1_inference = generate_level1_inference(
report_data["level1"]["hold_count"],
report_data["level1"]["go_to_level2_count"],
report_data["level1"]["hold_percentage"],
report_data["level1"]["level2_percentage"]
)

level1_conclusion = generate_level1_conclusion(
    report_data["level1"]["hold_count"],
    report_data["level1"]["go_to_level2_count"]
)
# =====================================================

# LEVEL 2

# =====================================================

level2_inference = generate_level2_inference(
report_data["level2"]["raise_count"],
report_data["level2"]["hold_count"],
report_data["level2"]["evaluation_percentage"]
)

level2_conclusion = generate_level2_conclusion(
    report_data["level2"]["raise_count"],
    report_data["level2"]["hold_count"],
    report_data["level2"]["evaluation_percentage"]
)
# =====================================================

# CHILLER 1

# =====================================================

ch1_inference = generate_ch1_inference(
report_data["ch1"]["hold_percentage"],
report_data["ch1"]["raise_percentage"],
report_data["ch1"]["reduce_percentage"]
)

ch1_conclusion = generate_ch1_conclusion(
    report_data["comparison_extended"]["dominant_action_ch1"],
    report_data["ch1"]["total_recommendations"]
)
# =====================================================

# CHILLER 2

# =====================================================

ch2_inference = generate_ch2_inference(
report_data["ch2"]["hold_percentage"],
report_data["ch2"]["raise_percentage"],
report_data["ch2"]["reduce_percentage"]
)

ch2_conclusion = generate_ch2_conclusion(
    report_data["comparison_extended"]["dominant_action_ch2"],
    report_data["ch2"]["total_recommendations"]
)
# =====================================================

# COMPARISON

# =====================================================

comparison_inference = generate_comparison_inference(
report_data["comparison"]["ch1_hold"],
report_data["comparison"]["ch2_hold"],
report_data["comparison"]["ch1_raise"],
report_data["comparison"]["ch2_raise"]
)

comparison_conclusion = generate_comparison_conclusion(
    report_data["comparison_extended"]["dominant_action_ch1"],
    report_data["comparison_extended"]["dominant_action_ch2"]
)
# =====================================================
# CH1 CURRENT SETPOINT
# =====================================================

ch1_current_inference = generate_ch1_current_inference(
    report_data["ch1_current"]["mean"],
    report_data["ch1_current"]["median"],
    report_data["ch1_current"]["min"],
    report_data["ch1_current"]["max"]
)

# =====================================================
# CH1 RECOMMENDED SETPOINT
# =====================================================

ch1_recommended_inference = generate_ch1_recommended_inference(
    report_data["ch1_recommended"]["mean"],
    report_data["ch1_recommended"]["median"],
    report_data["ch1_recommended"]["min"],
    report_data["ch1_recommended"]["max"]
)

# =====================================================
# CH2 CURRENT SETPOINT
# =====================================================

ch2_current_inference = generate_ch2_current_inference(
    report_data["ch2_current"]["mean"],
    report_data["ch2_current"]["median"],
    report_data["ch2_current"]["min"],
    report_data["ch2_current"]["max"]
)

# =====================================================
# CH2 RECOMMENDED SETPOINT
# =====================================================

ch2_recommended_inference = generate_ch2_recommended_inference(
    report_data["ch2_recommended"]["mean"],
    report_data["ch2_recommended"]["median"],
    report_data["ch2_recommended"]["min"],
    report_data["ch2_recommended"]["max"]
)

# =====================================================
# COMPARISON TAKEAWAY
# =====================================================

comparison_takeaway = generate_comparison_takeaway(
    report_data["comparison_extended"]["dominant_action_ch1"],
    report_data["comparison_extended"]["dominant_action_ch2"]
)

# =====================================================
# OVERALL TAKEAWAY
# =====================================================

overall_takeaway = generate_overall_takeaway(
    report_data["dataset"]["total_rows"],
    report_data["level0"]["pass_percentage"],
    report_data["comparison_extended"]["dominant_action_ch1"],
    report_data["comparison_extended"]["dominant_action_ch2"]
)

# =====================================================
# MAIN TAKEAWAY
# =====================================================

main_takeaway = generate_main_takeaway(
    report_data["level0"]["pass_percentage"],
    report_data["comparison_extended"]["dominant_action_ch1"],
    report_data["comparison_extended"]["dominant_action_ch2"]
)

# =====================================================

# LLM SECTIONS

# =====================================================

llm_sections = {

    "level0": {
        "inference": level0_inference,
        "conclusion": level0_conclusion
    },

    "level1": {
        "inference": level1_inference,
        "conclusion": level1_conclusion
    },

    "level2": {
        "inference": level2_inference,
        "conclusion": level2_conclusion
    },

    "ch1": {
        "inference": ch1_inference,
        "conclusion": ch1_conclusion
    },

    "ch2": {
        "inference": ch2_inference,
        "conclusion": ch2_conclusion
    },

    "comparison": {
        "inference": comparison_inference,
        "conclusion": comparison_conclusion
    },

    "ch1_current": {
        "inference": ch1_current_inference
    },

    "ch1_recommended": {
        "inference": ch1_recommended_inference
    },

    "ch2_current": {
        "inference": ch2_current_inference
    },

    "ch2_recommended": {
        "inference": ch2_recommended_inference
    },

    "comparison_takeaway": {
        "inference": comparison_takeaway
    },

    "overall_takeaway": {
        "inference": overall_takeaway
    },

    "main_takeaway": {
        "inference": main_takeaway
    }
}

# =====================================================

# GENERATE PDF

# =====================================================

generate_pdf(
report_data,
llm_sections,
"reports/report.pdf"
)
