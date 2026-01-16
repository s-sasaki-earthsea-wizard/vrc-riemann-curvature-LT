"""
軌道運動＝自由落下のmanimアニメーション

宇宙ステーションが地球の周りを「落ち続けている」ことを
直進経路と実際の軌道の差で可視化します。
"""

from manim import *
import numpy as np


class OrbitalFreefall(Scene):
    """宇宙ステーションが「落ち続けている」ことを示すアニメーション"""

    def construct(self):
        # 地球を作成（中央）
        earth = Circle(radius=1.5, color=BLUE, fill_opacity=0.7)
        earth.set_stroke(color=GREEN, width=3)
        earth_label = Text("地球", font_size=20)
        earth_label.next_to(earth, DOWN, buff=0.2)

        self.play(GrowFromCenter(earth), Write(earth_label))
        self.wait(0.3)

        # 軌道を点線で表示
        orbit_radius = 3.0
        orbit = Circle(radius=orbit_radius, color=WHITE, stroke_opacity=0.3)
        orbit.set_stroke(width=2)
        self.play(Create(orbit))

        # 宇宙ステーション（ボール）を作成
        station = Dot(radius=0.15, color=YELLOW)
        station_label = Text("宇宙ステーション", font_size=16, color=YELLOW)

        # 初期位置（右側）
        start_angle = 0
        station.move_to(RIGHT * orbit_radius)
        station_label.next_to(station, UP, buff=0.2)

        self.play(FadeIn(station), Write(station_label))
        self.wait(0.5)

        # 説明テキスト
        explanation = Text(
            "宇宙ステーションは「落ち続けている」",
            font_size=24,
        )
        explanation.to_edge(UP)
        self.play(Write(explanation))
        self.wait(0.5)

        # ステーションラベルをフェードアウト
        self.play(FadeOut(station_label))

        # 現在の角度を追跡
        current_angle = start_angle

        # 複数フレームで「直進 vs 落下 → 円軌道」を示す
        for i in range(4):
            target_angle = start_angle + i * PI / 2
            current_angle = self.show_freefall_frame(
                station, orbit_radius, current_angle, target_angle
            )

        # 結論
        conclusion = Text(
            "地面が曲がっているから、永遠に落ち続ける",
            font_size=24,
            color=GREEN,
        )
        conclusion.to_edge(UP)
        self.play(Transform(explanation, conclusion))
        self.wait(2)

    def show_freefall_frame(self, station, orbit_radius, current_angle, target_angle):
        """一つのフレームで直進経路と落下を示す（円弧上を移動）"""
        # まず目標位置まで円弧上を移動（必要な場合）
        angle_diff = target_angle - current_angle
        if abs(angle_diff) > 0.01:
            self.play(
                Rotate(
                    station,
                    angle=angle_diff,
                    about_point=ORIGIN,
                    rate_func=linear,
                ),
                run_time=0.8,
            )

        # 現在位置（target_angleの位置）
        current_pos = np.array([
            orbit_radius * np.cos(target_angle),
            orbit_radius * np.sin(target_angle),
            0,
        ])

        # 接線方向（直進方向）
        tangent = np.array([
            -np.sin(target_angle),
            np.cos(target_angle),
            0,
        ])

        # 直進した場合の位置（仮想）
        straight_distance = 1.5
        straight_pos = current_pos + tangent * straight_distance

        # 直進経路を点線で表示
        straight_path = DashedLine(
            current_pos,
            straight_pos,
            color=RED,
            dash_length=0.1,
        )
        straight_label = Text("直進経路", font_size=14, color=RED)
        straight_label.next_to(straight_path, tangent * 0.5, buff=0.1)

        self.play(
            Create(straight_path),
            FadeIn(straight_label),
            run_time=0.5,
        )

        # 重力（地球方向への落下）を示す矢印
        gravity_direction = -current_pos / np.linalg.norm(current_pos)
        gravity_arrow = Arrow(
            straight_pos,
            straight_pos + gravity_direction * 1.0,
            color=ORANGE,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.2,
        )
        gravity_label = Text("重力で落ちる", font_size=14, color=ORANGE)
        gravity_label.next_to(gravity_arrow, RIGHT, buff=0.1)

        self.play(
            GrowArrow(gravity_arrow),
            FadeIn(gravity_label),
            run_time=0.5,
        )
        self.wait(0.3)

        # 次の軌道上の位置（実際の経路）
        arc_angle = PI / 8
        next_angle = target_angle + arc_angle

        # 実際の軌道を示す曲線
        arc = Arc(
            radius=orbit_radius,
            start_angle=target_angle,
            angle=arc_angle,
            color=GREEN,
            stroke_width=4,
        )
        actual_label = Text("実際の経路", font_size=14, color=GREEN)
        mid_angle = target_angle + arc_angle / 2
        actual_label.move_to([
            (orbit_radius + 0.5) * np.cos(mid_angle),
            (orbit_radius + 0.5) * np.sin(mid_angle),
            0,
        ])

        # 円弧上を移動（Rotateを使用）
        self.play(
            Create(arc),
            FadeIn(actual_label),
            Rotate(
                station,
                angle=arc_angle,
                about_point=ORIGIN,
                rate_func=linear,
            ),
            run_time=1,
        )
        self.wait(0.3)

        # クリーンアップ
        self.play(
            FadeOut(straight_path),
            FadeOut(straight_label),
            FadeOut(gravity_arrow),
            FadeOut(gravity_label),
            FadeOut(arc),
            FadeOut(actual_label),
            run_time=0.3,
        )

        # 次のフレームの開始角度を返す
        return next_angle


class OrbitalFreefallSimple(Scene):
    """シンプル版：軌道運動＝自由落下"""

    def construct(self):
        # 地球を作成（中央）
        earth = Circle(radius=1.2, color=BLUE, fill_opacity=0.7)
        earth.set_stroke(color=GREEN, width=3)

        self.play(GrowFromCenter(earth))

        # 軌道
        orbit_radius = 2.8
        orbit = Circle(radius=orbit_radius, color=WHITE, stroke_opacity=0.2)
        self.play(Create(orbit))

        # 宇宙ステーション
        station = Dot(radius=0.12, color=YELLOW)
        station.move_to(RIGHT * orbit_radius)
        self.play(FadeIn(station))

        # 説明テキスト
        text = Text("重力がなければ直進する", font_size=22)
        text.to_edge(UP)
        self.play(Write(text))

        # 直進経路を示す
        straight_line = DashedLine(
            RIGHT * orbit_radius,
            RIGHT * orbit_radius + UP * 2.5,
            color=RED,
            dash_length=0.15,
        )
        self.play(Create(straight_line))
        self.wait(0.5)

        # 重力の矢印
        text2 = Text("でも重力で地球に向かって落ちる", font_size=22)
        text2.to_edge(UP)
        self.play(Transform(text, text2))

        gravity_arrow = Arrow(
            RIGHT * orbit_radius + UP * 1.5,
            RIGHT * orbit_radius + UP * 1.5 + LEFT * 1.2,
            color=ORANGE,
            stroke_width=4,
        )
        self.play(GrowArrow(gravity_arrow))
        self.wait(0.5)

        # 合成
        text3 = Text("合わさると...円軌道になる！", font_size=22, color=GREEN)
        text3.to_edge(UP)
        self.play(
            Transform(text, text3),
            FadeOut(straight_line),
            FadeOut(gravity_arrow),
        )

        # 円軌道を回るアニメーション
        self.play(
            Rotate(
                station,
                angle=2 * PI,
                about_point=ORIGIN,
                rate_func=linear,
            ),
            run_time=4,
        )

        # 結論
        conclusion = Text(
            "＝「落ち続けている」",
            font_size=26,
            color=YELLOW,
        )
        conclusion.to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(2)


if __name__ == "__main__":
    print("使用方法:")
    print("  manim -pql orbital_freefall.py OrbitalFreefall")
    print("  manim -pql orbital_freefall.py OrbitalFreefallSimple")
