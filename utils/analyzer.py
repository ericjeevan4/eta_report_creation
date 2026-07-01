import pandas as pd


def clean_numeric(series):
    """
    Convert to numeric and remove invalid values.
    Assumption:
    0 or negative values represent missing/invalid setpoints.
    """
    series = pd.to_numeric(series, errors="coerce")

    return series[
        (series.notna()) &
        (series > 0)
    ]


def analyze_csv(df):

    report_data = {}

    # =====================================================
    # DATASET OVERVIEW
    # =====================================================

    total_rows = len(df)
    total_columns = len(df.columns)

    report_data["dataset"] = {
        "total_rows": total_rows,
        "total_columns": total_columns
    }

    # =====================================================
    # LEVEL 0
    # =====================================================

    level0 = df["level0_action"].fillna("Null").value_counts()

    pass_count = int(level0.get("pass", 0))
    hold_count = int(level0.get("hold", 0))

    pass_pct = round(
        (pass_count / total_rows) * 100,
        1
    ) if total_rows else 0

    report_data["level0"] = {
        "pass_count": pass_count,
        "hold_count": hold_count,
        "pass_percentage": pass_pct
    }

    # =====================================================
    # LEVEL 1
    # =====================================================

    level1 = df["level1_action"].fillna("Null").value_counts()

    l1_hold = int(level1.get("hold", 0))
    l1_level2 = int(level1.get("go_to_level_2", 0))
    l1_reduce = int(level1.get("reduce_setpoint", 0))
    l1_null = int(level1.get("Null", 0))

    hold_pct_among_pass = round(
        (l1_hold / pass_count) * 100,
        1
    ) if pass_count else 0

    level2_pct_among_pass = round(
        (l1_level2 / pass_count) * 100,
        1
    ) if pass_count else 0

    report_data["level1"] = {
        "hold_count": l1_hold,
        "go_to_level2_count": l1_level2,
        "reduce_count": l1_reduce,
        "null_count": l1_null,
        "hold_percentage": hold_pct_among_pass,
        "level2_percentage": level2_pct_among_pass
    }

    # =====================================================
    # LEVEL 2
    # =====================================================

    level2 = df["level2_action"].fillna("Not reached").value_counts()

    raise_count = int(level2.get("raise_setpoint", 0))
    hold2_count = int(level2.get("hold", 0))
    not_reached_count = int(level2.get("Not reached", 0))

    level2_pct = round(
        (l1_level2 / total_rows) * 100,
        1
    ) if total_rows else 0

    report_data["level2"] = {
        "raise_count": raise_count,
        "hold_count": hold2_count,
        "not_reached_count": not_reached_count,
        "evaluation_percentage": level2_pct
    }

    # =====================================================
    # CHILLER 1
    # =====================================================

    ch1 = df["final_action_ch1"].fillna(
        "No recommendation"
    ).value_counts()

    ch1_hold = int(ch1.get("hold", 0))
    ch1_raise = int(ch1.get("raise_setpoint", 0))
    ch1_reduce = int(ch1.get("reduce_setpoint", 0))
    ch1_no = int(ch1.get("No recommendation", 0))

    ch1_total = (
        ch1_hold +
        ch1_raise +
        ch1_reduce
    )

    report_data["ch1"] = {
        "hold_count": ch1_hold,
        "raise_count": ch1_raise,
        "reduce_count": ch1_reduce,
        "no_recommendation": ch1_no,
        "total_recommendations": ch1_total,
        "hold_percentage": round((ch1_hold / ch1_total) * 100, 1) if ch1_total else 0,
        "raise_percentage": round((ch1_raise / ch1_total) * 100, 1) if ch1_total else 0,
        "reduce_percentage": round((ch1_reduce / ch1_total) * 100, 1) if ch1_total else 0,
    }

    # =====================================================
    # CH1 CURRENT SETPOINT
    # =====================================================

    ch1_current = clean_numeric(
        df["current_setpoint_ch1"]
    )

    report_data["ch1_current"] = {
        "mean": float(round(ch1_current.mean(), 2)) if len(ch1_current) else 0,
        "median": float(round(ch1_current.median(), 2)) if len(ch1_current) else 0,
        "min": float(round(ch1_current.min(), 2)) if len(ch1_current) else 0,
        "max": float(round(ch1_current.max(), 2)) if len(ch1_current) else 0
    }

    # =====================================================
    # CH1 RECOMMENDED SETPOINT
    # =====================================================

    ch1_rec = clean_numeric(
        df["recommended_setpoint_ch1"]
    )

    report_data["ch1_recommended"] = {
        "mean": float(round(ch1_rec.mean(), 2)) if len(ch1_rec) else 0,
        "median": float(round(ch1_rec.median(), 2)) if len(ch1_rec) else 0,
        "min": float(round(ch1_rec.min(), 2)) if len(ch1_rec) else 0,
        "max": float(round(ch1_rec.max(), 2)) if len(ch1_rec) else 0
    }

    # =====================================================
    # CHILLER 2
    # =====================================================

    ch2 = df["final_action_ch2"].fillna(
        "No recommendation"
    ).value_counts()

    ch2_hold = int(ch2.get("hold", 0))
    ch2_raise = int(ch2.get("raise_setpoint", 0))
    ch2_reduce = int(ch2.get("reduce_setpoint", 0))
    ch2_no = int(ch2.get("No recommendation", 0))

    ch2_total = (
        ch2_hold +
        ch2_raise +
        ch2_reduce
    )

    report_data["ch2"] = {
        "hold_count": ch2_hold,
        "raise_count": ch2_raise,
        "reduce_count": ch2_reduce,
        "no_recommendation": ch2_no,
        "total_recommendations": ch2_total,
        "hold_percentage": round((ch2_hold / ch2_total) * 100, 1) if ch2_total else 0,
        "raise_percentage": round((ch2_raise / ch2_total) * 100, 1) if ch2_total else 0,
        "reduce_percentage": round((ch2_reduce / ch2_total) * 100, 1) if ch2_total else 0,
    }

    # =====================================================
    # CH2 CURRENT SETPOINT
    # =====================================================

    ch2_current = clean_numeric(
        df["current_setpoint_ch2"]
    )

    report_data["ch2_current"] = {
        "mean": float(round(ch2_current.mean(), 2)) if len(ch2_current) else 0,
        "median": float(round(ch2_current.median(), 2)) if len(ch2_current) else 0,
        "min": float(round(ch2_current.min(), 2)) if len(ch2_current) else 0,
        "max": float(round(ch2_current.max(), 2)) if len(ch2_current) else 0
    }

    # =====================================================
    # CH2 RECOMMENDED SETPOINT
    # =====================================================

    ch2_rec = clean_numeric(
        df["recommended_setpoint_ch2"]
    )

    report_data["ch2_recommended"] = {
        "mean": float(round(ch2_rec.mean(), 2)) if len(ch2_rec) else 0,
        "median": float(round(ch2_rec.median(), 2)) if len(ch2_rec) else 0,
        "min": float(round(ch2_rec.min(), 2)) if len(ch2_rec) else 0,
        "max": float(round(ch2_rec.max(), 2)) if len(ch2_rec) else 0
    }

    # =====================================================
    # COMPARISON
    # =====================================================

    report_data["comparison"] = {
        "ch1_hold": ch1_hold,
        "ch2_hold": ch2_hold,
        "ch1_raise": ch1_raise,
        "ch2_raise": ch2_raise,
        "ch1_reduce": ch1_reduce,
        "ch2_reduce": ch2_reduce,
        "ch1_total": ch1_total,
        "ch2_total": ch2_total
    }

    # =====================================================
    # ADDITIONAL REPORT METRICS
    # =====================================================

    report_data["rare_reduction"] = {
        "total_reduce":
            ch1_reduce +
            ch2_reduce,

        "ch1_reduce":
            ch1_reduce,

        "ch2_reduce":
            ch2_reduce
    }

    report_data["comparison_extended"] = {

        "dominant_action_ch1":
            max(
                {
                    "hold": ch1_hold,
                    "raise_setpoint": ch1_raise,
                    "reduce_setpoint": ch1_reduce
                },
                key=lambda x: {
                    "hold": ch1_hold,
                    "raise_setpoint": ch1_raise,
                    "reduce_setpoint": ch1_reduce
                }[x]
            ),

        "dominant_action_ch2":
            max(
                {
                    "hold": ch2_hold,
                    "raise_setpoint": ch2_raise,
                    "reduce_setpoint": ch2_reduce
                },
                key=lambda x: {
                    "hold": ch2_hold,
                    "raise_setpoint": ch2_raise,
                    "reduce_setpoint": ch2_reduce
                }[x]
            )
    }

    report_data["hierarchy"] = {
        "total_rows": total_rows,
        "level0_pass": pass_count,
        "level1_hold": l1_hold,
        "level2_count": l1_level2,
        "level2_raise": raise_count,
        "level2_hold": hold2_count
    }

    return report_data