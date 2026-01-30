"""
収束しながら落下するボールのアニメーション
Balls falling while converging

横に並べた2つのボールが、ほんの少しだけ近づきながら落下する。
「平行に落ちる」という直感に反する現象を示し、
最後に「？」を表示して視聴者の疑問を誘う。

脚本L8-9に対応：
「実はこれ、厳密にはちょっと違うんです。」
"""

from manim import *


class ConvergingFall(Scene):
    """収束しながら落下するボール（軌跡付き） / Balls converging while falling with trails"""

    def construct(self):
        # 地面を作成（塗りつぶし）
        # Create ground (filled)
        ground = Rectangle(
            width=14,
            height=1.2,
            color="#4a3728",  # ダークブラウン
            fill_opacity=1.0,
        )
        ground.set_stroke(color="#8b7355", width=3)
        ground.move_to(DOWN * 3.1)

        # ボールを作成
        # Create balls
        ball_radius = 0.45
        initial_spacing = 2.5  # 初期間隔
        final_spacing = 2.1  # 着地時の間隔（少し狭くなる）
        start_height = 2.5

        ball_left = Circle(radius=ball_radius, color="#e74c3c", fill_opacity=0.85)
        ball_left.set_stroke(color="#ffffff", width=3)
        ball_left.move_to(LEFT * (initial_spacing / 2) + UP * start_height)

        ball_right = Circle(radius=ball_radius, color="#3498db", fill_opacity=0.85)
        ball_right.set_stroke(color="#ffffff", width=3)
        ball_right.move_to(RIGHT * (initial_spacing / 2) + UP * start_height)

        # 初期位置の水平破線（同じ高さを明示）
        # Dashed line showing initial height
        start_line = DashedLine(
            LEFT * 4 + UP * start_height,
            RIGHT * 4 + UP * start_height,
            color=GRAY,
            stroke_width=2,
            dash_length=0.2,
        )

        landing_y = -3.1 + 0.6 + ball_radius  # 地面上面 + ボール半径

        # 軌跡を追跡するためのTracedPath
        # TracedPath to draw ball trajectories
        trail_left = TracedPath(
            ball_left.get_center,
            stroke_color="#e74c3c",
            stroke_width=3,
            stroke_opacity=0.7,
        )
        trail_right = TracedPath(
            ball_right.get_center,
            stroke_color="#3498db",
            stroke_width=3,
            stroke_opacity=0.7,
        )

        # 地面を表示
        # Show ground
        self.add(ground)
        self.wait(0.2)

        # 初期位置の破線を表示
        # Show initial position line
        self.play(Create(start_line), run_time=0.3)

        # ボールを表示
        # Show balls
        self.play(
            FadeIn(ball_left, scale=0.5),
            FadeIn(ball_right, scale=0.5),
            run_time=0.5,
        )
        self.wait(0.3)

        # 軌跡の追跡を開始
        # Start tracking trails
        self.add(trail_left, trail_right)

        # 落下アニメーション（少し近づきながら）
        # Fall animation (converging slightly)
        self.play(
            ball_left.animate.move_to(LEFT * (final_spacing / 2) + UP * landing_y),
            ball_right.animate.move_to(RIGHT * (final_spacing / 2) + UP * landing_y),
            run_time=1.2,
            rate_func=rate_functions.ease_in_quad,
        )

        # 軌跡を破線に変換して強調
        # Convert trails to dashed lines for emphasis
        trail_left_dashed = DashedLine(
            LEFT * (initial_spacing / 2) + UP * start_height,
            LEFT * (final_spacing / 2) + UP * landing_y,
            color="#e74c3c",
            stroke_width=3,
            dash_length=0.15,
        )
        trail_right_dashed = DashedLine(
            RIGHT * (initial_spacing / 2) + UP * start_height,
            RIGHT * (final_spacing / 2) + UP * landing_y,
            color="#3498db",
            stroke_width=3,
            dash_length=0.15,
        )

        # 実線の軌跡を破線に置き換え
        # Replace solid trails with dashed lines
        self.remove(trail_left, trail_right)
        self.add(trail_left_dashed, trail_right_dashed)

        # 軽いバウンス
        # Light bounce
        self.play(
            ball_left.animate.shift(UP * 0.1),
            ball_right.animate.shift(UP * 0.1),
            run_time=0.08,
        )
        self.play(
            ball_left.animate.shift(DOWN * 0.1),
            ball_right.animate.shift(DOWN * 0.1),
            run_time=0.08,
        )

        # 少し待ってから「？」を表示
        # Wait, then show question mark
        self.wait(0.5)

        # はてなマークを表示（視聴者の疑問をくすぐる）
        # Show question mark to spark curiosity
        question_mark = Text("？", font_size=120, color=YELLOW)
        question_mark.move_to(UP * 1.0)

        self.play(
            FadeIn(question_mark, scale=1.5),
            run_time=0.4,
        )

        # はてなを少し揺らす演出
        # Subtle wobble effect on question mark
        self.play(
            question_mark.animate.scale(1.1),
            run_time=0.2,
            rate_func=rate_functions.ease_out_quad,
        )
        self.play(
            question_mark.animate.scale(1 / 1.1),
            run_time=0.2,
            rate_func=rate_functions.ease_in_quad,
        )

        # 静止
        # Hold
        self.wait(1.5)


class ConvergingFallWithArrows(Scene):
    """収束を矢印と軌跡で強調するバージョン / Version with arrows and trails emphasizing convergence"""

    def construct(self):
        # 地面を作成
        ground = Rectangle(
            width=14,
            height=1.2,
            color="#4a3728",
            fill_opacity=1.0,
        )
        ground.set_stroke(color="#8b7355", width=3)
        ground.move_to(DOWN * 3.1)

        # ボールを作成
        ball_radius = 0.45
        initial_spacing = 2.5
        final_spacing = 2.1
        start_height = 2.5

        ball_left = Circle(radius=ball_radius, color="#e74c3c", fill_opacity=0.85)
        ball_left.set_stroke(color="#ffffff", width=3)
        ball_left.move_to(LEFT * (initial_spacing / 2) + UP * start_height)

        ball_right = Circle(radius=ball_radius, color="#3498db", fill_opacity=0.85)
        ball_right.set_stroke(color="#ffffff", width=3)
        ball_right.move_to(RIGHT * (initial_spacing / 2) + UP * start_height)

        # 初期位置の水平破線
        start_line = DashedLine(
            LEFT * 4 + UP * start_height,
            RIGHT * 4 + UP * start_height,
            color=GRAY,
            stroke_width=2,
            dash_length=0.2,
        )

        landing_y = -3.1 + 0.6 + ball_radius

        # 軌跡を追跡するためのTracedPath
        # TracedPath to draw ball trajectories
        trail_left = TracedPath(
            ball_left.get_center,
            stroke_color="#e74c3c",
            stroke_width=3,
            stroke_opacity=0.7,
        )
        trail_right = TracedPath(
            ball_right.get_center,
            stroke_color="#3498db",
            stroke_width=3,
            stroke_opacity=0.7,
        )

        # 地面を表示
        self.add(ground)
        self.wait(0.2)

        # 初期位置の破線を表示
        self.play(Create(start_line), run_time=0.3)

        # ボールを表示
        self.play(
            FadeIn(ball_left, scale=0.5),
            FadeIn(ball_right, scale=0.5),
            run_time=0.5,
        )
        self.wait(0.3)

        # 軌跡の追跡を開始
        # Start tracking trails
        self.add(trail_left, trail_right)

        # 落下アニメーション
        self.play(
            ball_left.animate.move_to(LEFT * (final_spacing / 2) + UP * landing_y),
            ball_right.animate.move_to(RIGHT * (final_spacing / 2) + UP * landing_y),
            run_time=1.2,
            rate_func=rate_functions.ease_in_quad,
        )

        # 軌跡を破線に変換して強調
        # Convert trails to dashed lines for emphasis
        trail_left_dashed = DashedLine(
            LEFT * (initial_spacing / 2) + UP * start_height,
            LEFT * (final_spacing / 2) + UP * landing_y,
            color="#e74c3c",
            stroke_width=3,
            dash_length=0.15,
        )
        trail_right_dashed = DashedLine(
            RIGHT * (initial_spacing / 2) + UP * start_height,
            RIGHT * (final_spacing / 2) + UP * landing_y,
            color="#3498db",
            stroke_width=3,
            dash_length=0.15,
        )

        # 実線の軌跡を破線に置き換え
        # Replace solid trails with dashed lines
        self.remove(trail_left, trail_right)
        self.add(trail_left_dashed, trail_right_dashed)

        # 軽いバウンス
        self.play(
            ball_left.animate.shift(UP * 0.1),
            ball_right.animate.shift(UP * 0.1),
            run_time=0.08,
        )
        self.play(
            ball_left.animate.shift(DOWN * 0.1),
            ball_right.animate.shift(DOWN * 0.1),
            run_time=0.08,
        )

        self.wait(0.3)

        # 収束を示す矢印を追加
        # Add arrows showing convergence
        arrow_y = landing_y + 0.8
        left_arrow = Arrow(
            start=LEFT * 2.5 + UP * arrow_y,
            end=LEFT * 1.3 + UP * arrow_y,
            color=YELLOW,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.3,
        )
        right_arrow = Arrow(
            start=RIGHT * 2.5 + UP * arrow_y,
            end=RIGHT * 1.3 + UP * arrow_y,
            color=YELLOW,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.3,
        )

        self.play(
            GrowArrow(left_arrow),
            GrowArrow(right_arrow),
            run_time=0.4,
        )

        self.wait(0.3)

        # はてなマーク
        question_mark = Text("？", font_size=120, color=YELLOW)
        question_mark.move_to(UP * 1.0)

        self.play(
            FadeIn(question_mark, scale=1.5),
            run_time=0.4,
        )

        # 揺らす演出
        self.play(
            question_mark.animate.scale(1.1),
            run_time=0.2,
            rate_func=rate_functions.ease_out_quad,
        )
        self.play(
            question_mark.animate.scale(1 / 1.1),
            run_time=0.2,
            rate_func=rate_functions.ease_in_quad,
        )

        self.wait(1.5)


if __name__ == "__main__":
    # コマンドラインから実行する場合のヘルプ
    print("使用方法:")
    print("  manim -pql scripts/converging_fall.py ConvergingFall")
    print("  manim -pql scripts/converging_fall.py ConvergingFallWithArrows")
    print("")
    print("シーン説明:")
    print("  ConvergingFall          - 基本版（ボールが少し近づいて落下 + はてな）")
    print("  ConvergingFallWithArrows - 矢印付き版（収束を矢印で強調）")
    print("")
    print("脚本L8-9に対応:")
    print("  「実はこれ、厳密にはちょっと違うんです。」")
    print("  → ボールが平行ではなく、少し近づきながら落下することを示す")
