"""
潮汐力・測地線偏差・リーマン曲率の三位一体アニメーション
Tidal Force, Geodesic Deviation, Riemann Curvature Trinity Animation

3つの概念が同じものの異なる現れであることを視覚的に表現。
Visually demonstrates that these three concepts are different manifestations of the same thing.

yt_script.md L144-147 の解説用
"""

from manim import *


class TidalCurvatureTrinity(Scene):
    """
    潮汐力・測地線偏差・リーマン曲率が同じ概念であることを示す
    Shows that tidal force, geodesic deviation, and Riemann curvature are the same concept

    三角形配置で3つを表示し、中心で繋がっていることを表現
    Displays three concepts in a triangle, connected at the center
    """

    def construct(self):
        # ===== 色の定義 =====
        TIDAL_COLOR = BLUE
        GEODESIC_COLOR = GREEN
        RIEMANN_COLOR = ORANGE
        UNITY_COLOR = YELLOW

        # ===== 三角形の頂点位置 =====
        top_pos = UP * 2.0
        left_pos = DOWN * 1.2 + LEFT * 3.0
        right_pos = DOWN * 1.2 + RIGHT * 3.0
        center_pos = DOWN * 0.3

        # ===== 1. 潮汐力（上） =====
        tidal_icon = self._create_wave_icon().scale(0.5)
        tidal_label = Text("潮汐力", font_size=32, color=TIDAL_COLOR)
        tidal_label_en = Text("Tidal Force", font_size=18, color=GRAY)
        tidal_group = VGroup(
            tidal_icon,
            VGroup(tidal_label, tidal_label_en).arrange(DOWN, buff=0.05),
        ).arrange(DOWN, buff=0.2)
        tidal_group.move_to(top_pos)

        # ===== 2. 測地線偏差（左下） =====
        geodesic_icon = self._create_geodesic_icon().scale(0.5)
        geodesic_label = Text("測地線偏差", font_size=32, color=GEODESIC_COLOR)
        geodesic_label_en = Text("Geodesic Deviation", font_size=18, color=GRAY)
        geodesic_group = VGroup(
            geodesic_icon,
            VGroup(geodesic_label, geodesic_label_en).arrange(DOWN, buff=0.05),
        ).arrange(DOWN, buff=0.2)
        geodesic_group.move_to(left_pos)

        # ===== 3. リーマン曲率（右下） =====
        riemann_icon = self._create_curved_surface_icon().scale(0.5)
        riemann_label = Text("リーマン曲率", font_size=32, color=RIEMANN_COLOR)
        riemann_label_en = Text("Riemann Curvature", font_size=18, color=GRAY)
        riemann_group = VGroup(
            riemann_icon,
            VGroup(riemann_label, riemann_label_en).arrange(DOWN, buff=0.05),
        ).arrange(DOWN, buff=0.2)
        riemann_group.move_to(right_pos)

        # ===== 4. 接続線 =====
        line1 = Line(
            tidal_group.get_bottom() + DOWN * 0.1,
            center_pos,
            stroke_width=3,
            color=WHITE,
        )
        line2 = Line(
            geodesic_group.get_right() + RIGHT * 0.1,
            center_pos,
            stroke_width=3,
            color=WHITE,
        )
        line3 = Line(
            riemann_group.get_left() + LEFT * 0.1,
            center_pos,
            stroke_width=3,
            color=WHITE,
        )

        # ===== 5. 中心の等号 =====
        equiv_symbol = MathTex(r"\equiv", font_size=60, color=UNITY_COLOR)
        equiv_symbol.move_to(center_pos)

        # ===== 6. 結論テキスト =====
        conclusion = Text(
            "同じ概念の異なる現れ",
            font_size=28,
            color=UNITY_COLOR,
        )
        conclusion_en = Text(
            "Different manifestations of the same concept",
            font_size=16,
            color=GRAY,
        )
        conclusion_group = VGroup(conclusion, conclusion_en).arrange(DOWN, buff=0.05)
        conclusion_group.to_edge(DOWN, buff=0.5)

        # ===== アニメーション（合計約23秒） =====
        # [0-5秒] 3つのアイコン/テキストが順番に登場
        self.play(FadeIn(tidal_group, shift=DOWN * 0.3), run_time=1.5)
        self.play(FadeIn(geodesic_group, shift=RIGHT * 0.3), run_time=1.5)
        self.play(FadeIn(riemann_group, shift=LEFT * 0.3), run_time=1.5)
        self.wait(0.8)

        # [5-12秒] 3つを結ぶ線がアニメーションで描かれ、中心に「≡」が出現
        self.play(
            Create(line1),
            Create(line2),
            Create(line3),
            run_time=2.5,
        )
        self.wait(0.5)

        self.play(
            FadeIn(equiv_symbol, scale=1.5),
            run_time=1.2,
        )
        self.wait(1.0)

        # [12-20秒] 中心から光が広がり、3つが同じ色に染まる
        # 結論テキスト表示
        self.play(
            tidal_label.animate.set_color(UNITY_COLOR),
            geodesic_label.animate.set_color(UNITY_COLOR),
            riemann_label.animate.set_color(UNITY_COLOR),
            line1.animate.set_color(UNITY_COLOR),
            line2.animate.set_color(UNITY_COLOR),
            line3.animate.set_color(UNITY_COLOR),
            run_time=2.0,
        )

        self.play(FadeIn(conclusion_group, shift=UP * 0.2), run_time=1.2)
        self.wait(7.5)

        # [20-23秒] フェードアウト
        self.play(
            FadeOut(tidal_group),
            FadeOut(geodesic_group),
            FadeOut(riemann_group),
            FadeOut(line1),
            FadeOut(line2),
            FadeOut(line3),
            FadeOut(equiv_symbol),
            FadeOut(conclusion_group),
            run_time=1.5,
        )
        self.wait(0.3)

    def _create_wave_icon(self) -> VGroup:
        """波のアイコンを作成（潮汐力を表現）"""
        wave = VGroup()
        for i in range(3):
            curve = FunctionGraph(
                lambda x: 0.3 * np.sin(2 * x),
                x_range=[-1.5, 1.5],
                color=BLUE,
                stroke_width=3,
            )
            curve.shift(DOWN * i * 0.4)
            wave.add(curve)
        return wave

    def _create_geodesic_icon(self) -> VGroup:
        """測地線偏差のアイコンを作成（2本の曲がる線）"""
        # 2本の線が離れていく様子
        line1 = FunctionGraph(
            lambda x: 0.1 * x**2,
            x_range=[-1.5, 1.5],
            color=GREEN,
            stroke_width=3,
        )
        line2 = FunctionGraph(
            lambda x: -0.1 * x**2,
            x_range=[-1.5, 1.5],
            color=GREEN,
            stroke_width=3,
        )
        # 矢印を追加
        arrow1 = Arrow(
            line1.get_end() + LEFT * 0.3,
            line1.get_end() + RIGHT * 0.1 + UP * 0.2,
            buff=0,
            color=GREEN,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.3,
        )
        arrow2 = Arrow(
            line2.get_end() + LEFT * 0.3,
            line2.get_end() + RIGHT * 0.1 + DOWN * 0.2,
            buff=0,
            color=GREEN,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.3,
        )
        return VGroup(line1, line2, arrow1, arrow2)

    def _create_curved_surface_icon(self) -> VGroup:
        """曲面のアイコンを作成（リーマン曲率を表現）"""
        # 曲面を表すグリッド線
        surface = VGroup()

        # 横線（曲がっている）
        for i in range(-2, 3):
            curve = FunctionGraph(
                lambda x, y_offset=i * 0.4: 0.15 * np.sin(x) + y_offset,
                x_range=[-1.5, 1.5],
                color=ORANGE,
                stroke_width=2,
            )
            surface.add(curve)

        # 縦線（曲がっている）
        for i in range(-3, 4):
            x_val = i * 0.5
            points = [
                np.array([x_val, 0.15 * np.sin(x_val) + y, 0])
                for y in np.linspace(-0.8, 0.8, 20)
            ]
            line = VMobject(color=ORANGE, stroke_width=2)
            line.set_points_smoothly(points)
            surface.add(line)

        return surface


if __name__ == "__main__":
    print("使用方法 / Usage:")
    print("  manim -pql scripts/tidal_curvature_trinity.py TidalCurvatureTrinity")
    print("")
    print("シーン説明 / Scene descriptions:")
    print("  TidalCurvatureTrinity - 潮汐力・測地線偏差・リーマン曲率の三位一体")
    print("                          Trinity of tidal force, geodesic deviation, and Riemann curvature")
    print("")
    print("オプション / Options:")
    print("  -p: プレビュー / Preview")
    print("  -ql: 低品質（高速） / Low quality (fast)")
    print("  -qm: 中品質 / Medium quality")
    print("  -qh: 高品質 / High quality")
    print("  -qk: 4K品質 / 4K quality")
