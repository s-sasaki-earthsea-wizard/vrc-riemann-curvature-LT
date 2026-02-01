"""
リーマン曲率テンソルの紹介アニメーション
Riemann Curvature Tensor Introduction Animation

リーマン曲率テンソルの式をさっと表示するだけのシンプルなアニメーション。
深入りせず、式の形だけを見せる。
（リーマンの肖像は動画編集で追加）

A simple animation that briefly shows the Riemann curvature tensor formula.
No deep explanation, just shows the form of the equation.
(Riemann's portrait will be added in video editing)

yt_script.md L133-140 の解説用
"""

from manim import *


class RiemannCurvatureIntro(Scene):
    """
    リーマン曲率テンソルの式を簡潔に表示
    Briefly displays the Riemann curvature tensor formula

    式の形だけを見せて、すぐにフェードアウト
    Shows the form of the equation and fades out
    """

    def construct(self):
        # ===== タイトル =====
        title = Text("リーマン曲率", font_size=40)
        title_en = Text("Riemann Curvature", font_size=24, color=GRAY)
        title_group = VGroup(title, title_en).arrange(DOWN, buff=0.15)
        title_group.to_edge(UP, buff=0.8)

        self.play(Write(title_group), run_time=1.0)
        self.wait(0.5)

        # ===== リーマン曲率テンソルの式 =====
        # R^a_bcd = ∂_c Γ^a_db - ∂_d Γ^a_cb + Γ^a_ce Γ^e_db - Γ^a_de Γ^e_cb
        formula = MathTex(
            r"R^{a}_{\ bcd}",
            r"=",
            r"\partial_c \Gamma^{a}_{\ db}",
            r"-",
            r"\partial_d \Gamma^{a}_{\ cb}",
            r"+",
            r"\Gamma^{a}_{\ ce} \Gamma^{e}_{\ db}",
            r"-",
            r"\Gamma^{a}_{\ de} \Gamma^{e}_{\ cb}",
            font_size=42,
        )
        formula.set_color_by_tex(r"R^{a}_{\ bcd}", YELLOW)

        # 式を中央やや下に配置
        formula.move_to(ORIGIN)

        # ===== 補足テキスト =====
        note = Text("19世紀にリーマンが考案", font_size=20, color=GRAY_B)
        note_en = Text("Developed by Riemann in the 19th century", font_size=14, color=GRAY)
        note_group = VGroup(note, note_en).arrange(DOWN, buff=0.05)
        note_group.next_to(formula, DOWN, buff=0.8)

        # ===== アニメーション =====
        # 式をフェードイン
        self.play(FadeIn(formula, shift=UP * 0.3), run_time=1.2)
        self.wait(0.3)

        # 補足テキストをフェードイン
        self.play(FadeIn(note_group, shift=UP * 0.2), run_time=0.8)
        self.wait(1.5)

        # すべてフェードアウト
        self.play(
            FadeOut(title_group),
            FadeOut(formula),
            FadeOut(note_group),
            run_time=1.0,
        )
        self.wait(0.3)


if __name__ == "__main__":
    print("使用方法 / Usage:")
    print("  manim -pql scripts/riemann_curvature_intro.py RiemannCurvatureIntro")
    print("")
    print("シーン説明 / Scene descriptions:")
    print("  RiemannCurvatureIntro - リーマン曲率テンソルの式を簡潔に表示")
    print("                          Briefly shows the Riemann curvature tensor formula")
    print("")
    print("オプション / Options:")
    print("  -p: プレビュー / Preview")
    print("  -ql: 低品質（高速） / Low quality (fast)")
    print("  -qm: 中品質 / Medium quality")
    print("  -qh: 高品質 / High quality")
    print("  -qk: 4K品質 / 4K quality")
