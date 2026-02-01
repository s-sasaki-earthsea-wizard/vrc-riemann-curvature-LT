"""
測地線偏差のアニメーション
Geodesic Deviation Animation

2本の曲がった測地線が少しずつ伸びながら、間隔が変化していく様子を可視化。
同一曲線上で収束（converging）から発散（diverging）へと変化。

Visualizes two curved geodesics growing gradually while their separation changes.
Shows converging then diverging on the same continuous curves.

yt_script.md L126-131 の解説用
"""

from manim import *
import numpy as np


class GeodesicDeviation(Scene):
    """
    曲がった測地線の偏差アニメーション
    Animation of geodesic deviation with curved paths

    2本の曲がった測地線が伸びていく過程で、
    最初は間隔が狭まり（収束）、その後広がる（発散）様子を表示
    Shows two curved geodesics where separation first decreases (converging)
    then increases (diverging) as they grow
    """

    def construct(self):
        # ===== タイトル =====
        title = Text("測地線偏差", font_size=32)
        title_en = Text("Geodesic Deviation", font_size=20, color=GRAY)
        title_group = VGroup(title, title_en).arrange(DOWN, buff=0.1)
        title_group.to_edge(UP, buff=0.4)

        self.play(Write(title_group))
        self.wait(0.5)

        # ===== 曲がった測地線のパラメータ =====
        # 曲線の基準点
        center_x = 0
        start_y = -2.5
        end_y = 2.5

        # 間隔のパラメータ
        # t=0: 広い, t=0.5: 最も狭い, t=1: 再び広い
        initial_separation = 2.5   # 開始時の間隔
        min_separation = 0.4       # 最小間隔（中間点）
        final_separation = 3.0     # 終了時の間隔

        def separation_at(t):
            """
            tに応じた間隔を計算（滑らかなcosine補間）
            t=0: initial, t=0.5: min, t=1: final
            """
            if t <= 0.5:
                # 0 -> 0.5: 収束（間隔が狭まる）
                # cosine補間で滑らかに
                ratio = (1 - np.cos(t * 2 * PI)) / 2  # 0->1 滑らかに
                return initial_separation + (min_separation - initial_separation) * ratio
            else:
                # 0.5 -> 1: 発散（間隔が広がる）
                # cosine補間で滑らかに
                local_t = (t - 0.5) * 2  # 0->1に正規化
                ratio = (1 - np.cos(local_t * PI)) / 2  # 0->1 滑らかに
                return min_separation + (final_separation - min_separation) * ratio

        def geodesic1_path(t):
            """左側の測地線（滑らかな曲線）"""
            y = start_y + t * (end_y - start_y)
            sep = separation_at(t)
            # 滑らかなS字カーブを追加
            curve = 0.5 * np.sin(t * PI)
            x = center_x - sep / 2 - curve
            return np.array([x, y, 0])

        def geodesic2_path(t):
            """右側の測地線（滑らかな曲線）"""
            y = start_y + t * (end_y - start_y)
            sep = separation_at(t)
            # 滑らかなS字カーブを追加
            curve = 0.5 * np.sin(t * PI)
            x = center_x + sep / 2 + curve
            return np.array([x, y, 0])

        # ===== 測地線ラベル =====
        geodesic_label1 = Text("測地線", font_size=16, color=RED_A)
        geodesic_label1_en = Text("Geodesic", font_size=12, color=RED_A)
        geodesic_group1 = VGroup(geodesic_label1, geodesic_label1_en).arrange(DOWN, buff=0.03)

        geodesic_label2 = Text("測地線", font_size=16, color=BLUE_A)
        geodesic_label2_en = Text("Geodesic", font_size=12, color=BLUE_A)
        geodesic_group2 = VGroup(geodesic_label2, geodesic_label2_en).arrange(DOWN, buff=0.03)

        # ===== 間隔を示す矢印（3箇所：開始、中間、終了） =====
        # 開始時の間隔（t=0）
        start_arrow = DoubleArrow(
            geodesic1_path(0),
            geodesic2_path(0),
            color=GREEN_C,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.08,
            buff=0.1,
        )
        start_label = Text("広い / Wide", font_size=12, color=GREEN_C)
        start_label.next_to(start_arrow, DOWN, buff=0.15)

        # 中間点の間隔（t=0.5、最小）
        mid_arrow = DoubleArrow(
            geodesic1_path(0.5),
            geodesic2_path(0.5),
            color=ORANGE,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.2,
            buff=0.1,
        )
        mid_label = Text("狭い / Narrow", font_size=12, color=ORANGE)
        mid_label.next_to(mid_arrow, LEFT, buff=0.15)

        # 終了時の間隔（t=1）
        end_arrow = DoubleArrow(
            geodesic1_path(1),
            geodesic2_path(1),
            color=GREEN_C,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.08,
            buff=0.1,
        )
        end_label = Text("広い / Wide", font_size=12, color=GREEN_C)
        end_label.next_to(end_arrow, UP, buff=0.15)

        # ===== 開始点を表示 =====
        start_dot1 = Dot(geodesic1_path(0), radius=0.08, color=RED_C)
        start_dot2 = Dot(geodesic2_path(0), radius=0.08, color=BLUE_C)

        self.play(
            FadeIn(start_dot1, scale=0.5),
            FadeIn(start_dot2, scale=0.5),
            run_time=0.5,
        )

        # 開始時の間隔を表示
        self.play(
            GrowArrow(start_arrow),
            Write(start_label),
            run_time=0.6,
        )
        self.wait(0.3)

        # ===== 測地線を伸ばすアニメーション（前半：収束） =====
        explain_text = Text("収束：間隔が狭まる", font_size=20, color=YELLOW)
        explain_text_en = Text("Converging: Separation decreases", font_size=14, color=YELLOW_A)
        explain_group = VGroup(explain_text, explain_text_en).arrange(DOWN, buff=0.05)
        explain_group.to_edge(DOWN, buff=0.5)

        self.play(Write(explain_group), run_time=0.5)

        # 前半の測地線（t=0 to 0.5）
        geodesic1_first = ParametricFunction(
            geodesic1_path, t_range=[0, 0.5], color=RED_C, stroke_width=4
        )
        geodesic2_first = ParametricFunction(
            geodesic2_path, t_range=[0, 0.5], color=BLUE_C, stroke_width=4
        )

        self.play(
            Create(geodesic1_first),
            Create(geodesic2_first),
            run_time=2.0,
            rate_func=rate_functions.linear,
        )

        # 中間点にドットを追加
        mid_dot1 = Dot(geodesic1_path(0.5), radius=0.08, color=RED_C)
        mid_dot2 = Dot(geodesic2_path(0.5), radius=0.08, color=BLUE_C)

        self.play(
            FadeIn(mid_dot1, scale=0.5),
            FadeIn(mid_dot2, scale=0.5),
            run_time=0.3,
        )

        # 中間点の間隔を表示
        self.play(
            GrowArrow(mid_arrow),
            Write(mid_label),
            run_time=0.6,
        )
        self.wait(0.5)

        # ===== 測地線を伸ばすアニメーション（後半：発散） =====
        explain_text2 = Text("発散：間隔が広がる", font_size=20, color=YELLOW)
        explain_text2_en = Text("Diverging: Separation increases", font_size=14, color=YELLOW_A)
        explain_group2 = VGroup(explain_text2, explain_text2_en).arrange(DOWN, buff=0.05)
        explain_group2.to_edge(DOWN, buff=0.5)

        self.play(Transform(explain_group, explain_group2), run_time=0.5)

        # 後半の測地線（t=0.5 to 1）
        geodesic1_second = ParametricFunction(
            geodesic1_path, t_range=[0.5, 1], color=RED_C, stroke_width=4
        )
        geodesic2_second = ParametricFunction(
            geodesic2_path, t_range=[0.5, 1], color=BLUE_C, stroke_width=4
        )

        self.play(
            Create(geodesic1_second),
            Create(geodesic2_second),
            run_time=2.0,
            rate_func=rate_functions.linear,
        )

        # 終了点にドットを追加
        end_dot1 = Dot(geodesic1_path(1), radius=0.08, color=RED_C)
        end_dot2 = Dot(geodesic2_path(1), radius=0.08, color=BLUE_C)

        self.play(
            FadeIn(end_dot1, scale=0.5),
            FadeIn(end_dot2, scale=0.5),
            run_time=0.3,
        )

        # ラベルを配置
        geodesic_group1.next_to(geodesic1_path(0.25), LEFT, buff=0.2)
        geodesic_group2.next_to(geodesic2_path(0.25), RIGHT, buff=0.2)

        self.play(
            Write(geodesic_group1),
            Write(geodesic_group2),
            run_time=0.5,
        )

        # 終了時の間隔を表示
        self.play(
            GrowArrow(end_arrow),
            Write(end_label),
            run_time=0.6,
        )
        self.wait(0.5)

        # ===== 結論 =====
        conclusion = Text("これが「測地線偏差」", font_size=24, color=WHITE)
        conclusion_en = Text('This is "Geodesic Deviation"', font_size=16, color=GRAY)
        conclusion_group = VGroup(conclusion, conclusion_en).arrange(DOWN, buff=0.08)
        conclusion_group.to_edge(DOWN, buff=0.5)

        self.play(Transform(explain_group, conclusion_group))
        self.wait(2)


if __name__ == "__main__":
    print("使用方法 / Usage:")
    print("  manim -pql scripts/geodesic_deviation.py GeodesicDeviation")
    print("")
    print("シーン説明 / Scene descriptions:")
    print("  GeodesicDeviation - 曲がった測地線で収束→発散を連続表示")
    print("                      Curved geodesics showing converging then diverging")
    print("")
    print("オプション / Options:")
    print("  -p: プレビュー / Preview")
    print("  -ql: 低品質（高速） / Low quality (fast)")
    print("  -qm: 中品質 / Medium quality")
    print("  -qh: 高品質 / High quality")
    print("  -qk: 4K品質 / 4K quality")
