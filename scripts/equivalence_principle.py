"""
等価原理のmanimアニメーション
Manim animation: The Equivalence Principle

落下するエレベーターの中で、重力と加速度が打ち消し合い、
中にいる人にとって重力が「消えた」ように感じられることを可視化します。

Visualizes how gravity and acceleration cancel out in a falling elevator,
making the person inside feel as if gravity has "disappeared".
"""

from manim import *


class EquivalencePrinciple(Scene):
    """
    等価原理：落下するエレベーターの中で重力が消える
    Equivalence Principle: Gravity "disappears" in a falling elevator
    """

    def construct(self):
        # タイトル / Title
        title = Text(
            "等価原理 / Equivalence Principle",
            font_size=32,
        )
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # エレベーター（箱）を作成 / Create elevator (box)
        elevator_width = 3.0
        elevator_height = 4.0
        elevator = Rectangle(
            width=elevator_width,
            height=elevator_height,
            color=GRAY,
            fill_opacity=0.2,
        )
        elevator.set_stroke(color=WHITE, width=4)
        elevator.move_to(ORIGIN)

        # 窓のない箱であることを示す / Indicate windowless box
        no_window_text = Text(
            "窓のない箱 / Windowless box",
            font_size=18,
            color=GRAY,
        )
        no_window_text.next_to(elevator, RIGHT, buff=0.3)

        self.play(Create(elevator), FadeIn(no_window_text))
        self.wait(0.3)

        # 人（シンプルな棒人間）を作成 / Create person (simple stick figure)
        person = self.create_stick_figure()
        person.move_to(elevator.get_center() + DOWN * 0.5)

        self.play(FadeIn(person))
        self.wait(0.5)

        # フェーズ1：静止している状態 / Phase 1: At rest
        phase1_text = Text(
            "静止状態 / At rest",
            font_size=24,
            color=BLUE,
        )
        phase1_text.next_to(title, DOWN, buff=0.3)
        self.play(Write(phase1_text))

        # 重力の矢印（人に作用） / Gravity arrow (acting on person)
        gravity_arrow = Arrow(
            person.get_center() + RIGHT * 0.8,
            person.get_center() + RIGHT * 0.8 + DOWN * 1.2,
            color=RED,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.2,
        )
        gravity_label = Text("重力 g", font_size=16, color=RED)
        gravity_label_en = Text("Gravity", font_size=12, color=RED)
        gravity_label.next_to(gravity_arrow, RIGHT, buff=0.1)
        gravity_label_en.next_to(gravity_label, DOWN, buff=0.05)
        gravity_group = VGroup(gravity_label, gravity_label_en)

        # 床からの抗力（反作用） / Normal force from floor
        normal_arrow = Arrow(
            person.get_center() + LEFT * 0.8 + DOWN * 0.8,
            person.get_center() + LEFT * 0.8 + UP * 0.4,
            color=GREEN,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.2,
        )
        normal_label = Text("床からの力", font_size=16, color=GREEN)
        normal_label_en = Text("Normal force", font_size=12, color=GREEN)
        normal_label.next_to(normal_arrow, LEFT, buff=0.1)
        normal_label_en.next_to(normal_label, DOWN, buff=0.05)
        normal_group = VGroup(normal_label, normal_label_en)

        self.play(
            GrowArrow(gravity_arrow),
            FadeIn(gravity_group),
        )
        self.play(
            GrowArrow(normal_arrow),
            FadeIn(normal_group),
        )
        self.wait(1)

        # フェーズ2：自由落下開始 / Phase 2: Free fall begins
        phase2_text = Text(
            "自由落下！ / Free fall!",
            font_size=24,
            color=ORANGE,
        )
        phase2_text.next_to(title, DOWN, buff=0.3)
        self.play(Transform(phase1_text, phase2_text))

        # 床の抗力が消える / Normal force disappears
        self.play(
            FadeOut(normal_arrow),
            FadeOut(normal_group),
        )
        self.wait(0.3)

        # 「窓のない箱」テキストをフェードアウト
        self.play(FadeOut(no_window_text))

        # エレベーターと人を一緒に落下させる / Drop elevator and person together
        fall_group = VGroup(elevator, person, gravity_arrow, gravity_group)

        # 落下中、エレベーター内の人の視点では... / From the person's perspective inside...
        perspective_text = Text(
            "エレベーター内の視点 / Inside view",
            font_size=20,
            color=YELLOW,
        )
        perspective_text.to_edge(LEFT).shift(UP * 2)
        self.play(FadeIn(perspective_text))

        # 落下アニメーション / Fall animation
        self.play(
            fall_group.animate.shift(DOWN * 2),
            run_time=1.5,
            rate_func=rate_functions.ease_in_quad,
        )
        self.wait(0.5)

        # フェーズ3：エレベーター基準で見ると / Phase 3: In the elevator's reference frame
        phase3_text = Text(
            "エレベーター基準では... / In the elevator's frame...",
            font_size=24,
            color=YELLOW,
        )
        phase3_text.next_to(title, DOWN, buff=0.3)
        self.play(Transform(phase1_text, phase3_text))

        # 慣性力（見かけの力）の矢印を追加 / Add inertial (pseudo) force arrow
        inertial_arrow = Arrow(
            person.get_center() + LEFT * 0.8,
            person.get_center() + LEFT * 0.8 + UP * 1.2,
            color=BLUE,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.2,
        )
        inertial_label = Text("慣性力 -ma", font_size=16, color=BLUE)
        inertial_label_en = Text("Inertial force", font_size=12, color=BLUE)
        inertial_label.next_to(inertial_arrow, LEFT, buff=0.1)
        inertial_label_en.next_to(inertial_label, DOWN, buff=0.05)
        inertial_group = VGroup(inertial_label, inertial_label_en)

        self.play(
            GrowArrow(inertial_arrow),
            FadeIn(inertial_group),
        )
        self.wait(0.5)

        # 力の打ち消し合いを強調 / Emphasize force cancellation
        cancel_text = Text(
            "重力 + 慣性力 = 0",
            font_size=28,
            color=GREEN,
        )
        cancel_text_en = Text(
            "Gravity + Inertial force = 0",
            font_size=20,
            color=GREEN,
        )
        cancel_group = VGroup(cancel_text, cancel_text_en).arrange(DOWN, buff=0.1)
        cancel_group.to_edge(RIGHT).shift(UP * 0.5)

        self.play(Write(cancel_group))
        self.wait(0.5)

        # 矢印を打ち消す視覚効果 / Visual effect of arrows canceling
        cross1 = Cross(gravity_arrow, stroke_width=6, color=WHITE)
        cross2 = Cross(inertial_arrow, stroke_width=6, color=WHITE)

        self.play(
            Create(cross1),
            Create(cross2),
        )
        self.wait(0.5)

        # 矢印をフェードアウト / Fade out arrows
        self.play(
            FadeOut(gravity_arrow),
            FadeOut(gravity_group),
            FadeOut(inertial_arrow),
            FadeOut(inertial_group),
            FadeOut(cross1),
            FadeOut(cross2),
            FadeOut(cancel_group),
            FadeOut(perspective_text),
        )

        # フェーズ4：結論 / Phase 4: Conclusion
        # 人が浮いている状態を示す / Show person floating
        self.play(
            person.animate.move_to(elevator.get_center()),
            run_time=0.8,
        )

        conclusion_text = Text(
            "重力が「消えた」ように感じる",
            font_size=26,
            color=GREEN,
        )
        conclusion_text_en = Text(
            "Gravity seems to have 'disappeared'",
            font_size=20,
            color=GREEN,
        )
        conclusion_group = VGroup(conclusion_text, conclusion_text_en).arrange(DOWN, buff=0.1)
        conclusion_group.next_to(title, DOWN, buff=0.3)
        self.play(Transform(phase1_text, conclusion_group))
        self.wait(1)

        # 等価原理のテキスト / Equivalence principle text
        principle_text = Text(
            "重力と加速度は局所的に区別できない",
            font_size=24,
            color=YELLOW,
        )
        principle_text_en = Text(
            "Gravity and acceleration are locally indistinguishable",
            font_size=18,
            color=YELLOW,
        )
        principle_group = VGroup(principle_text, principle_text_en).arrange(DOWN, buff=0.1)
        principle_group.to_edge(DOWN, buff=0.8)

        box = SurroundingRectangle(
            principle_group,
            color=YELLOW,
            buff=0.2,
            corner_radius=0.1,
        )

        self.play(
            Write(principle_group),
            Create(box),
        )
        self.wait(2)

        # 最終メッセージ / Final message
        final_text = Text(
            "これが「等価原理」",
            font_size=32,
            color=WHITE,
        )
        final_text_en = Text(
            "This is the 'Equivalence Principle'",
            font_size=24,
            color=WHITE,
        )
        final_group = VGroup(final_text, final_text_en).arrange(DOWN, buff=0.1)
        final_group.next_to(principle_group, UP, buff=0.5)

        self.play(Write(final_group))
        self.wait(2)

    def create_stick_figure(self):
        """
        シンプルな棒人間を作成
        Create a simple stick figure
        """
        # 頭 / Head
        head = Circle(radius=0.2, color=WHITE, fill_opacity=0.5)
        head.set_stroke(color=WHITE, width=2)

        # 体 / Body
        body = Line(ORIGIN, DOWN * 0.6, color=WHITE, stroke_width=3)
        body.next_to(head, DOWN, buff=0)

        # 腕 / Arms
        left_arm = Line(ORIGIN, LEFT * 0.3 + DOWN * 0.2, color=WHITE, stroke_width=3)
        right_arm = Line(ORIGIN, RIGHT * 0.3 + DOWN * 0.2, color=WHITE, stroke_width=3)
        arm_start = body.get_start() + DOWN * 0.1
        left_arm.move_to(arm_start, aligned_edge=UP)
        right_arm.move_to(arm_start, aligned_edge=UP)

        # 足 / Legs
        left_leg = Line(ORIGIN, LEFT * 0.2 + DOWN * 0.4, color=WHITE, stroke_width=3)
        right_leg = Line(ORIGIN, RIGHT * 0.2 + DOWN * 0.4, color=WHITE, stroke_width=3)
        leg_start = body.get_end()
        left_leg.move_to(leg_start, aligned_edge=UP)
        right_leg.move_to(leg_start, aligned_edge=UP)

        return VGroup(head, body, left_arm, right_arm, left_leg, right_leg)


class EquivalencePrincipleSimple(Scene):
    """
    シンプル版：等価原理
    Simple version: Equivalence Principle
    """

    def construct(self):
        # 左右に2つのシナリオを並べる / Show two scenarios side by side
        # 左：地上で静止 / Left: At rest on ground
        # 右：自由落下中 / Right: In free fall

        # タイトル / Title
        title = Text(
            "どちらも同じに見える / Both look the same",
            font_size=28,
        )
        title.to_edge(UP)
        self.play(Write(title))

        # 左側：宇宙空間で静止 / Left: At rest in space
        left_box = Rectangle(width=2.5, height=3.5, color=GRAY)
        left_box.set_stroke(width=3)
        left_box.move_to(LEFT * 3)

        left_label = Text("宇宙空間で静止", font_size=16)
        left_label_en = Text("At rest in space", font_size=12)
        left_labels = VGroup(left_label, left_label_en).arrange(DOWN, buff=0.05)
        left_labels.next_to(left_box, UP, buff=0.2)

        left_person = self.create_simple_person()
        left_person.scale(0.8)
        left_person.move_to(left_box.get_center())

        # 右側：自由落下中 / Right: In free fall
        right_box = Rectangle(width=2.5, height=3.5, color=GRAY)
        right_box.set_stroke(width=3)
        right_box.move_to(RIGHT * 3)

        right_label = Text("自由落下中", font_size=16)
        right_label_en = Text("In free fall", font_size=12)
        right_labels = VGroup(right_label, right_label_en).arrange(DOWN, buff=0.05)
        right_labels.next_to(right_box, UP, buff=0.2)

        right_person = self.create_simple_person()
        right_person.scale(0.8)
        right_person.move_to(right_box.get_center())

        # 表示 / Display
        self.play(
            Create(left_box),
            Create(right_box),
            FadeIn(left_labels),
            FadeIn(right_labels),
        )
        self.play(
            FadeIn(left_person),
            FadeIn(right_person),
        )
        self.wait(0.5)

        # 両方で人が浮いている / Person floating in both
        floating_text = Text(
            "どちらも無重力に感じる",
            font_size=22,
            color=GREEN,
        )
        floating_text_en = Text(
            "Both feel weightless",
            font_size=16,
            color=GREEN,
        )
        floating_group = VGroup(floating_text, floating_text_en).arrange(DOWN, buff=0.1)
        floating_group.next_to(title, DOWN, buff=0.3)

        self.play(Write(floating_group))
        self.wait(1)

        # 区別できないことを強調 / Emphasize indistinguishability
        question = Text(
            "窓がなければ、区別できない！",
            font_size=24,
            color=YELLOW,
        )
        question_en = Text(
            "Without windows, they cannot be distinguished!",
            font_size=18,
            color=YELLOW,
        )
        question_group = VGroup(question, question_en).arrange(DOWN, buff=0.1)
        question_group.to_edge(DOWN, buff=0.8)

        box = SurroundingRectangle(question_group, color=YELLOW, buff=0.2)
        self.play(
            Write(question_group),
            Create(box),
        )
        self.wait(2)

    def create_simple_person(self):
        """シンプルな人の図形 / Simple person shape"""
        head = Circle(radius=0.15, color=WHITE, fill_opacity=0.5)
        head.set_stroke(color=WHITE, width=2)
        body = Line(ORIGIN, DOWN * 0.5, color=WHITE, stroke_width=3)
        body.next_to(head, DOWN, buff=0)
        return VGroup(head, body)


if __name__ == "__main__":
    # 使用方法 / Usage
    print("使用方法 / Usage:")
    print("  manim -pql scripts/equivalence_principle.py EquivalencePrinciple")
    print("  manim -pql scripts/equivalence_principle.py EquivalencePrincipleSimple")
    print("")
    print("シーン説明 / Scene descriptions:")
    print("  EquivalencePrinciple       - フル版：落下エレベーターで重力が打ち消し合う")
    print("                               Full version: Gravity cancels in falling elevator")
    print("  EquivalencePrincipleSimple - シンプル版：2つのシナリオの比較")
    print("                               Simple version: Comparison of two scenarios")
