import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"


def rewrite_professionally(text):

    prompt = f"""
You are a professional technical report writer.

STRICT RULES:

1. Rewrite professionally.
2. Keep all numbers unchanged.
3. Keep all facts unchanged.
4. Do NOT add information.
5. Do NOT remove information.
6. Do NOT infer anything.
7. Do NOT add recommendations.
8. Do NOT add future work.
9. Do NOT add headings.
10. Do NOT add bullets.
11. Return ONLY the rewritten paragraph.

Text:

{text}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()

    return response.json()["response"].strip()


# =====================================================
# LEVEL 0
# =====================================================

def generate_level0_inference(
        total_rows,
        pass_count,
        hold_count):

    pass_pct = round(
        (pass_count / total_rows) * 100,
        1
    ) if total_rows else 0

    text = f"""
Approximately {pass_pct}% of observations pass Level-0.

A total of {pass_count} observations pass Level-0, while {hold_count} observations are held.

Level-0 rarely blocks recommendation generation and primarily acts as a preliminary screening stage.
"""

    return rewrite_professionally(text)


def generate_level0_conclusion(
        pass_count,
        hold_count):

    text = f"""
A total of {pass_count} observations pass Level-0, while {hold_count} observations are held.

These results summarize the Level-0 screening outcome.
"""

    return rewrite_professionally(text)


# =====================================================
# LEVEL 1
# =====================================================

def generate_level1_inference(
        hold_count,
        level2_count,
        hold_percentage,
        level2_percentage):

    text = f"""
Among observations passing Level-0, {hold_percentage}% are held at Level-1.

A total of {hold_count} observations are held at Level-1.

A total of {level2_count} observations proceed to Level-2, representing {level2_percentage}% of Level-0 passes.

Level-1 acts as an intermediate decision layer.
"""

    return rewrite_professionally(text)


def generate_level1_conclusion(
        hold_count,
        level2_count):

    text = f"""
Level-1 holds {hold_count} observations and forwards {level2_count} observations to Level-2.

These results summarize the Level-1 decision outcome.
"""

    return rewrite_professionally(text)


# =====================================================
# LEVEL 2
# =====================================================

def generate_level2_inference(
        raise_count,
        hold_count,
        evaluation_percentage):

    text = f"""
A total of {raise_count} observations receive a raise setpoint action at Level-2.

A total of {hold_count} observations are held at Level-2.

Only {evaluation_percentage}% of observations require Level-2 evaluation.
"""

    return rewrite_professionally(text)


def generate_level2_conclusion(
        raise_count,
        hold_count,
        evaluation_percentage):

    text = f"""
A total of {raise_count} observations receive raise setpoint actions and {hold_count} observations receive hold actions at Level-2.

Level-2 evaluation is performed for {evaluation_percentage}% of the overall observations.

These results summarize the Level-2 decision outcome.
"""

    return rewrite_professionally(text)


# =====================================================
# CHILLER 1
# =====================================================

def generate_ch1_inference(
        hold_percentage,
        raise_percentage,
        reduce_percentage):

    text = f"""
For Chiller 1, {hold_percentage}% of recommendations are hold actions.

{raise_percentage}% of recommendations are raise setpoint actions.

{reduce_percentage}% of recommendations are reduce setpoint actions.
"""

    return rewrite_professionally(text)


def generate_ch1_conclusion(
        dominant_action,
        recommendation_count):

    text = f"""
The dominant recommendation issued for Chiller 1 is {dominant_action}.

A total of {recommendation_count} recommendations were generated for Chiller 1.
"""

    return rewrite_professionally(text)


# =====================================================
# CHILLER 2
# =====================================================

def generate_ch2_inference(
        hold_percentage,
        raise_percentage,
        reduce_percentage):

    text = f"""
For Chiller 2, {hold_percentage}% of recommendations are hold actions.

{raise_percentage}% of recommendations are raise setpoint actions.

{reduce_percentage}% of recommendations are reduce setpoint actions.
"""

    return rewrite_professionally(text)


def generate_ch2_conclusion(
        dominant_action,
        recommendation_count):

    text = f"""
The dominant recommendation issued for Chiller 2 is {dominant_action}.

A total of {recommendation_count} recommendations were generated for Chiller 2.
"""

    return rewrite_professionally(text)


# =====================================================
# COMPARISON
# =====================================================

def generate_comparison_inference(
        ch1_hold,
        ch2_hold,
        ch1_raise,
        ch2_raise):

    text = f"""
Chiller 1 receives {ch1_hold} hold recommendations and {ch1_raise} raise recommendations.

Chiller 2 receives {ch2_hold} hold recommendations and {ch2_raise} raise recommendations.
"""

    return rewrite_professionally(text)


def generate_comparison_conclusion(
        dominant_ch1,
        dominant_ch2):

    text = f"""
The dominant recommendation for Chiller 1 is {dominant_ch1}.

The dominant recommendation for Chiller 2 is {dominant_ch2}.

The comparison highlights differences in recommendation behaviour between the two chillers.
"""

    return rewrite_professionally(text)

def generate_ch1_current_inference(
        mean,
        median,
        minimum,
        maximum):

    text = f"""
Chiller 1 current operating setpoints range from {minimum}°C to {maximum}°C.

The mean operating setpoint is {mean}°C and the median operating setpoint is {median}°C.

These statistics summarize the observed operating behaviour of Chiller 1.
"""

    return rewrite_professionally(text)

def generate_ch1_recommended_inference(
        mean,
        median,
        minimum,
        maximum):

    text = f"""
Recommended Chiller 1 setpoints range from {minimum}°C to {maximum}°C.

The mean recommended setpoint is {mean}°C and the median recommended setpoint is {median}°C.

These values represent the recommendations generated by the optimization framework.
"""

    return rewrite_professionally(text)

def generate_ch2_current_inference(
        mean,
        median,
        minimum,
        maximum):

    text = f"""
Chiller 2 current operating setpoints range from {minimum}°C to {maximum}°C.

The mean operating setpoint is {mean}°C and the median operating setpoint is {median}°C.

These statistics summarize the observed operating behaviour of Chiller 2.
"""

    return rewrite_professionally(text)

def generate_ch2_recommended_inference(
        mean,
        median,
        minimum,
        maximum):

    text = f"""
Recommended Chiller 2 setpoints range from {minimum}°C to {maximum}°C.

The mean recommended setpoint is {mean}°C and the median recommended setpoint is {median}°C.

These values represent the recommendations generated by the optimization framework.
"""

    return rewrite_professionally(text)

def generate_comparison_takeaway(
        ch1_action,
        ch2_action):

    text = f"""
The dominant recommendation for Chiller 1 is {ch1_action}.

The dominant recommendation for Chiller 2 is {ch2_action}.

The recommendation patterns indicate operational differences between the two chillers.
"""

    return rewrite_professionally(text)

def generate_overall_takeaway(
        total_rows,
        pass_pct,
        ch1_action,
        ch2_action):

    text = f"""
The dataset contains {total_rows} observations.

Level-0 passes account for {pass_pct}% of observations.

The dominant Chiller 1 recommendation is {ch1_action}.

The dominant Chiller 2 recommendation is {ch2_action}.

These results summarize the overall behaviour of the recommendation framework.
"""
    return rewrite_professionally(text)
# =====================================================
# MAIN TAKEAWAY
# =====================================================

def generate_main_takeaway(
        pass_percentage,
        ch1_action,
        ch2_action):

    text = f"""
Level-0 achieves a pass rate of {pass_percentage}%.

The dominant recommendation for Chiller 1 is {ch1_action}.

The dominant recommendation for Chiller 2 is {ch2_action}.

These observations summarize the most significant outcomes of the recommendation process.
"""

    return rewrite_professionally(text)

    