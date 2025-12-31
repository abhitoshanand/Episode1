""" Manim scene collection for: "The Physics of Value" — Episode 1 File: physics_of_value_manim.py

How to render (example): manim -p -ql physics_of_value_manim.py TitleScene manim -p -ql physics_of_value_manim.py ArithmeticExampleScene

Notes:

Designed for Manim Community (manim >=0.13). Uses from manim import * API.

Scenes are modular; run any scene or create a short composition scene at bottom.


Structure:

TitleScene: intro with logo and voice-timing markers

MoneyAsCertificateScene: coins/notes morph into claim-checks

WorkEnergyScene: farmer/factory/doctor icons animated with energy flows

ArithmeticExampleScene: 100 goods / 100 money -> 1; then 100 / 200 -> 0.5 with bar charts

InflationScene: tickets vs seats metaphor with tickets popping in

SourcesOfValueScene: animated list of energy, labor, materials, tech with growing factory

PolicyScene: monetary expansion vs capacity expansion with split-screen comparison

ConservationLimitsScene: entropy/metaphor, gradual fade to waste

SummaryScene: bullet summary with emphasis animations

TeaserScene: MV=PQ intro and motion hint to Episode 2


Customize colors, fonts and timings below. """

from manim import *

----------------------------

Global style options

----------------------------

TITLE_COLOR = "#F8F8FF" ACCENT = "#66D9EF" BG_COLOR = "#0F172A" PAPER_COLOR = "#FFF7E6" COIN_COLOR = "#F2C94C" NOTE_COLOR = "#A3E635"

config.background_color = BG_COLOR

----------------------------

Helper functions & icon factory

----------------------------

def make_note(width=2.5, height=1.2, text="100"): note = RoundedRectangle(corner_radius=0.15, width=width, height=height).set_fill(NOTE_COLOR, opacity=0.95).set_stroke(width=0) label = Text(text, font_size=36, weight=BOLD) return VGroup(note, label)

def make_coin(radius=0.5, text="COIN"): disc = Circle(radius=radius).set_fill(COIN_COLOR, opacity=1).set_stroke(width=0) label = Text(text, font_size=30, weight=BOLD) return VGroup(disc, label)

def make_icon_box(label_text, icon_shape=None): box = RoundedRectangle(corner_radius=0.12, width=2.5, height=1.2).set_fill(WHITE, opacity=0.06).set_stroke(width=1, opacity=0.6) label = Text(label_text, font_size=24) if icon_shape is not None: return VGroup(box, VGroup(icon_shape, label).arrange(RIGHT, buff=0.4)) return VGroup(box, label)

class Breathing: def init(self, mobject, scale_factor=1.02, run_time=1.0): self.mobject = mobject self.scale_factor = scale_factor self.run_time = run_time

def start(self, scene):
    scene.play(self.mobject.animate.scale(self.scale_factor), rate_func=there_and_back, run_time=self.run_time)

----------------------------

Scenes

----------------------------

class TitleScene(Scene): def construct(self): title = Text("The Physics of Value", font_size=64, weight=BOLD) subtitle = Text("Episode 1 — Money as Stored Work", font_size=28).next_to(title, DOWN) channel = Text("Manan", font_size=28).to_corner(UR)

atom = Circle(radius=0.8).set_stroke(ACCENT, width=3)
    electrons = VGroup(*[Dot().move_to(0.8 * RIGHT).rotate_about_origin(angle) for angle in [0, TAU/3, 2*TAU/3]]).set_color(ACCENT)
    logo = VGroup(atom, electrons, Text("A", font_size=36, weight=BOLD)).arrange()

    bg = Rectangle(width=FRAME_WIDTH, height=FRAME_HEIGHT).set_fill(BG_COLOR, opacity=1)
    self.add(bg)

    self.play(FadeIn(title, shift=UP), Write(subtitle), FadeIn(channel))
    self.play(LaggedStart(FadeIn(logo), logo.animate.shift(UP*0.8)), run_time=1.6)
    self.wait(1.2)

    tagline = Text("A physics lens on economics", font_size=22).next_to(subtitle, DOWN)
    self.play(Write(tagline), run_time=1.2)
    self.wait(0.8)

    mic = Circle(radius=0.15).set_fill(WHITE, opacity=1).to_edge(DL)
    self.play(GrowFromCenter(mic), run_time=0.6)

    self.play(FadeOut(title, shift=UP), FadeOut(tagline), FadeOut(logo), FadeOut(channel))
    self.wait(0.5)

class MoneyAsCertificateScene(Scene): def construct(self): header = Text("Money = Claim Check on Work", font_size=44, weight=BOLD).to_edge(UP) self.play(Write(header))

note = make_note(text="Note").scale(1.2).to_edge(LEFT)
    coin = make_coin(text="Coin").next_to(note, DOWN, buff=0.6)

    product_box = RoundedRectangle(corner_radius=0.12, width=4, height=2).set_fill(PAPER_COLOR, opacity=0.95).to_edge(RIGHT)
    product_label = Text("Food, Medicine, Electricity, Shoes", font_size=24).move_to(product_box.get_center())
    product = VGroup(product_box, product_label)

    self.play(FadeIn(note, shift=LEFT), FadeIn(coin, shift=LEFT))
    self.play(FadeIn(product, shift=RIGHT))
    self.wait(0.6)

    ticket = Rectangle(width=1.6, height=0.9).set_fill("#E6EEF8", opacity=0.95).set_stroke(width=1).move_to(note.get_center())
    ticket_label = Text("Claim Check", font_size=20).move_to(ticket.get_center())
    ticket_group = VGroup(ticket, ticket_label)

    arrow = Arrow(start=note.get_right(), end=product.get_left(), buff=0.2)

    self.play(Transform(note, ticket_group), Transform(coin, ticket_group.copy().next_to(ticket_group, DOWN, buff=0.3)), Create(arrow))
    self.wait(0.6)

    caption = Text("A certificate claiming a share of produced goods and services", font_size=20).next_to(product, DOWN)
    self.play(Write(caption))
    self.wait(1.0)

    self.play(self.camera.frame.animate.shift(LEFT*0.6), run_time=1.0)
    Breathing(ticket_group, scale_factor=1.03, run_time=1.2).start(self)
    self.wait(0.6)

    self.play(FadeOut(ticket_group), FadeOut(product), FadeOut(arrow), FadeOut(caption), FadeOut(coin))
    self.play(FadeOut(header))

class WorkEnergyScene(Scene): def construct(self): header = Text("Work & Energy: Physical transformations produce value", font_size=38).to_edge(UP) self.play(Write(header))

farmer = make_icon_box("Farmer", icon_shape=Square(side_length=0.5))
    factory = make_icon_box("Factory", icon_shape=Triangle())
    doctor = make_icon_box("Doctor", icon_shape=Circle(radius=0.25))

    group = VGroup(farmer, factory, doctor).arrange(RIGHT, buff=1.2).scale(0.9).next_to(header, DOWN, buff=0.6)
    self.play(LaggedStart(*[FadeIn(m) for m in group], lag_ratio=0.2), run_time=1.2)

    flows = VGroup()
    for i, icon in enumerate(group):
        bar = Rectangle(width=0.3, height=2.0).next_to(icon, DOWN, buff=0.4)
        bar.set_fill(ACCENT, opacity=0.8).set_stroke(width=0)
        flows.add(bar)
    flows.arrange(RIGHT, buff=2.0)
    flows.next_to(group, DOWN, buff=0.4)

    self.play(LaggedStartMap(GrowFromEdge, flows, lambda m: m, run_time=1.4))
    self.wait(0.4)

    for _ in range(3):
        for bar, icon in zip(flows, group):
            self.play(bar.animate.stretch(1.05, 1, about_point=bar.get_top()), run_time=0.25)
    self.wait(0.4)

    products = VGroup(RoundedRectangle(corner_radius=0.12, width=3, height=1.2).set_fill(PAPER_COLOR, opacity=0.95), Text("Products & Services", font_size=22)).arrange()
    arrow = Arrow(start=group.get_bottom(), end=products.get_left(), buff=0.5)
    products.next_to(arrow, RIGHT)

    self.play(Create(arrow), FadeIn(products, shift=RIGHT))
    self.wait(0.6)

    note = Text("Value emerges from transforming inputs (energy + labour + materials)", font_size=20).next_to(products, DOWN)
    self.play(Write(note))
    self.wait(1.0)

    self.play(FadeOut(group), FadeOut(flows), FadeOut(products), FadeOut(arrow), FadeOut(note), FadeOut(header))

class ArithmeticExampleScene(Scene): def construct(self): header = Text("Simple arithmetic: goods / claim checks", font_size=36).to_edge(UP) self.play(Write(header))

goods_eq = Text("Goods = 100 units", font_size=28)
    money_eq = Text("Money supply = 100 claim checks", font_size=28)
    frac = Text("100 / 100 = 1 unit per check", font_size=28)

    layout = VGroup(goods_eq, money_eq, frac).arrange(DOWN, buff=0.6).move_to(ORIGIN)
    self.play(LaggedStart(*[Write(m) for m in layout], lag_ratio=0.3))
    self.wait(0.8)

    goods_bar = Rectangle(width=1.0, height=2.0).set_fill(ACCENT, opacity=0.9).shift(LEFT*1.3)
    money_bar = Rectangle(width=1.0, height=2.0).set_fill(PAPER_COLOR, opacity=0.9).shift(RIGHT*1.3)
    goods_label = Text("Goods: 100", font_size=20).next_to(goods_bar, UP)
    money_label = Text("Money: 100", font_size=20).next_to(money_bar, UP)

    self.play(Transform(layout, VGroup(goods_label, money_label).arrange(RIGHT, buff=3).to_edge(UP)))
    self.play(GrowFromCenter(goods_bar), GrowFromCenter(money_bar), run_time=1.0)
    self.wait(0.6)

    result = Text("100/100 = 1", font_size=32).to_edge(DOWN)
    self.play(Write(result), run_time=0.8)
    self.wait(0.8)

    money_new = Text("Money supply = 200 claim checks", font_size=28)
    frac2 = Text("100 / 200 = 0.5 unit per check", font_size=28)
    self.play(Transform(money_eq, money_new), Transform(frac, frac2), run_time=1.0)

    money_bar.generate_target()
    money_bar.target.stretch_to_fit_height(4.5)
    note = Text("Production unchanged, money doubled → purchasing power falls", font_size=20).next_to(result, UP)
    self.play(MoveToTarget(money_bar), Write(note), run_time=1.2)
    self.wait(1.0)

    slice_before = Rectangle(width=0.9, height=1.5).set_fill(WHITE, opacity=0.6).move_to(goods_bar.get_center())
    slice_after = Rectangle(width=0.9, height=0.75).set_fill(WHITE, opacity=0.6).move_to(goods_bar.get_center()).shift(LEFT*0.4+DOWN*0.4)
    self.play(FadeIn(slice_before), run_time=0.5)
    self.play(Transform(slice_before, slice_after), run_time=1.0)
    self.wait(0.8)

    infl_label = Text("Inflation: less purchasing power per claim check", font_size=20).next_to(result, DOWN)
    self.play(Write(infl_label))
    self.wait(1.0)

    self.play(FadeOut(goods_bar), FadeOut(money_bar), FadeOut(slice_before), FadeOut(goods_label), FadeOut(money_label), FadeOut(result), FadeOut(header), FadeOut(infl_label), FadeOut(note))

class InflationScene(Scene): def construct(self): header = Text("Tickets vs Seats — a simple metaphor", font_size=34).to_edge(UP) self.play(Write(header))

seats = VGroup(*[Square(side_length=0.6).set_fill(PAPER_COLOR, opacity=0.95) for _ in range(6)]).arrange_in_grid(rows=2, cols=3, buff=0.3)
    seats_label = Text("6 seats", font_size=20).next_to(seats, DOWN)
    seats.to_edge(LEFT)

    tickets = VGroup(*[Rectangle(width=0.6, height=0.3).set_fill(ACCENT, opacity=0.95) for _ in range(6)]).arrange(DOWN, buff=0.2).to_edge(RIGHT)
    tickets_label = Text("6 tickets", font_size=20).next_to(tickets, UP)

    self.play(FadeIn(seats), Write(seats_label), FadeIn(tickets), Write(tickets_label))
    self.wait(0.6)

    more_tickets = VGroup(*[Rectangle(width=0.6, height=0.3).set_fill(COIN_COLOR, opacity=0.95) for _ in range(6)]).arrange(DOWN, buff=0.2).next_to(tickets, DOWN, buff=0.2)
    self.play(LaggedStartMap(FadeIn, more_tickets, lag_ratio=0.1), run_time=1.0)
    new_label = Text("12 tickets for 6 seats → each ticket's claim weakens", font_size=20).next_to(seats, DOWN)
    self.play(Write(new_label))
    self.wait(1.0)

    for i, seat in enumerate(seats):
        t = VGroup(tickets, more_tickets)[i]
        self.play(t.animate.move_to(seat.get_center()).scale(0.9), run_time=0.2)
    self.wait(0.6)

    for t in VGroup(more_tickets):
        self.play(t.animate.shift(UP*0.4), run_time=0.2)
    self.play(LaggedStart(*[FadeOut(t) for t in more_tickets], lag_ratio=0.08), run_time=0.8)
    self.wait(0.6)

    self.play(FadeOut(seats), FadeOut(tickets), FadeOut(more_tickets), FadeOut(new_label), FadeOut(header), FadeOut(seats_label), FadeOut(tickets_label))

class SourcesOfValueScene(Scene): def construct(self): header = Text("Where real value comes from", font_size=36).to_edge(UP) bullets = VGroup( Text("• Labour", font_size=26), Text("• Energy inputs", font_size=26), Text("• Natural resources", font_size=26), Text("• Technology & organization", font_size=26), ).arrange(DOWN, aligned_edge=LEFT, buff=0.6).to_edge(LEFT) self.play(Write(header)) self.play(LaggedStart(*[Write(b) for b in bullets], lag_ratio=0.3)) self.wait(0.8)

cap_before = Rectangle(width=3, height=1.0).set_fill(ACCENT, opacity=0.8).to_corner(UR)
    cap_text_before = Text("Capacity: 100", font_size=20).next_to(cap_before, LEFT)
    self.play(FadeIn(cap_before), Write(cap_text_before))
    self.wait(0.6)

    invest_arrow = Arrow(start=cap_before.get_bottom(), end=cap_before.get_bottom()+DOWN*1.5)
    cap_after = Rectangle(width=4.5, height=1.0).set_fill(ACCENT, opacity=0.9).next_to(cap_before, DOWN, buff=1.2)
    cap_text_after = Text("Capacity: 150", font_size=20).next_to(cap_after, LEFT)
    self.play(GrowFromCenter(invest_arrow), Transform(cap_before, cap_after), Transform(cap_text_before, cap_text_after))
    self.wait(0.8)

    expl = Text("Money matched with productive investment can increase real output.", font_size=20).to_edge(DOWN)
    self.play(Write(expl))
    self.wait(1.0)
    self.play(FadeOut(header), FadeOut(bullets), FadeOut(cap_after), FadeOut(cap_text_after), FadeOut(expl))

class PolicyScene(Scene): def construct(self): header = Text("Policy choices: money vs capacity", font_size=36).to_edge(UP) left = Text("Monetary expansion only", font_size=22).to_edge(LEFT).shift(DOWN0.6) right = Text("Monetary + Productive investment", font_size=22).to_edge(RIGHT).shift(DOWN0.6) self.play(Write(header)) self.play(Write(left), Write(right))

left_money = VGroup(make_note(text="Note").scale(0.9), Text("Money ↑", font_size=24)).arrange(DOWN).to_edge(LEFT).shift(UP*0.6)
    left_prices = Text("Prices ↑", font_size=28).next_to(left_money, DOWN)

    right_money = make_note(text="Note").scale(0.9).to_edge(RIGHT).shift(UP*0.6)
    right_factory = Rectangle(width=2, height=1).set_fill(ACCENT, opacity=0.8).next_to(right_money, DOWN, buff=0.4)
    right_prices = Text("Prices stable or ↓", font_size=24).next_to(right_factory, DOWN)

    self.play(FadeIn(left_money), Write(left_prices))
    self.play(FadeIn(right_money), FadeIn(right_factory), Write(right_prices))
    self.wait(1.0)

    admin = Text("Printing money: fast (admin)\nBuilding capacity: slow (resources & time)", font_size=18).next_to(header, DOWN)
    self.play(Write(admin))
    self.wait(1.0)

    self.play(FadeOut(header), FadeOut(left), FadeOut(right), FadeOut(left_money), FadeOut(left_prices), FadeOut(right_money), FadeOut(right_factory), FadeOut(right_prices), FadeOut(admin))

class ConservationLimitsScene(Scene): def construct(self): header = Text("Physical limits: conservation & entropy", font_size=34).to_edge(UP) self.play(Write(header))

resource = Rectangle(width=4, height=1).set_fill("#BDE0FE", opacity=0.9).set_stroke(width=0).move_to(ORIGIN+UP*0.6)
    resource_label = Text("Concentrated resources (energy & materials)", font_size=20).next_to(resource, UP)
    output = Rectangle(width=4, height=1).set_fill("#FBE7C6", opacity=0.9).next_to(resource, DOWN, buff=1.2)
    output_label = Text("Useful products + waste", font_size=20).next_to(output, DOWN)

    arrow = Arrow(resource.get_bottom(), output.get_top(), buff=0.2)
    self.play(FadeIn(resource), Write(resource_label), Create(arrow), FadeIn(output), Write(output_label))
    self.wait(0.8)

    entropy = Text("Each transformation increases entropy — limits to growth and sustainability", font_size=18).next_to(output_label, DOWN)
    self.play(Write(entropy))
    self.wait(1.0)

    self.play(FadeOut(header), FadeOut(resource), FadeOut(resource_label), FadeOut(arrow), FadeOut(output), FadeOut(output_label), FadeOut(entropy))

class SummaryScene(Scene): def construct(self): header = Text("Summary — Key takeaways", font_size=40).to_edge(UP) points = VGroup( Text("1. Money = claim on stored work (not value itself)", font_size=24), Text("2. More money without more production → inflation", font_size=24), Text("3. Real growth needs energy, labour, materials, tech", font_size=24), Text("4. Monetary policy stabilizes, but doesn't create physical goods", font_size=24) ).arrange(DOWN, buff=0.6).next_to(header, DOWN)

self.play(Write(header))
    for p in points:
        self.play(FadeIn(p, shift=UP), run_time=0.8)
        self.wait(0.4)

    emphasize = Text("Think in terms of physical constraints — money is the accounting, production is the physics.", font_size=20).to_edge(DOWN)
    self.play(Write(emphasize))
    self.wait(1.2)
    self.play(FadeOut(header), FadeOut(points), FadeOut(emphasize))

class TeaserScene(Scene): def construct(self): header = Text("Next: How money moves — MV = PQ", font_size=36).to_edge(UP) mv = Text("M × V = P × Q", font_size=64) note = Text("Money supply × velocity = price level × quantity of goods", font_size=20).next_to(mv, DOWN)

self.play(Write(header))
    self.play(Write(mv))
    self.play(Write(note))
    self.wait(1.2)

    cta = Text("Subscribe for Episode Two", font_size=28).to_edge(DOWN)
    self.play(FadeIn(cta))
    self.wait(0.8)
    self.play(FadeOut(header), FadeOut(mv), FadeOut(note), FadeOut(cta))

End of file
