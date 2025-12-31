from manim import *

class PhysicsOfValue(Scene):
    def construct(self):
        # Scene 1: Title and Introduction (0:00 - 0:20)
        self.scene_intro()
        
        # Scene 2: Money's Intrinsic Value Question (0:20 - 1:00)
        self.scene_intrinsic_value()
        
        # Scene 3: Work and Energy Concept (1:00 - 1:40)
        self.scene_work_energy()
        
        # Scene 4: Arithmetic Example - Part 1 (1:40 - 2:30)
        self.scene_arithmetic_setup()
        
        # Scene 5: Arithmetic Example - Part 2 (2:30 - 3:20)
        self.scene_inflation_demo()
        
        # Scene 6: Bookkeeping Logic (3:20 - 4:00)
        self.scene_tickets_analogy()
        
        # Scene 7: Sources of Real Value (4:00 - 5:00)
        self.scene_real_value_sources()
        
        # Scene 8: Production Changes (5:00 - 6:00)
        self.scene_production_effects()
        
        # Scene 9: Monetary Policy Discussion (6:00 - 7:30)
        self.scene_monetary_policy()
        
        # Scene 10: Physical Constraints (7:30 - 8:30)
        self.scene_physical_limits()
        
        # Scene 11: Summary (8:30 - 9:30)
        self.scene_summary()
        
        # Scene 12: Next Episode Teaser (9:30 - 10:00)
        self.scene_next_episode()

    def scene_intro(self):
        # Title card with elegant animation
        title = Text("The Physics of Value", font_size=56, weight=BOLD, gradient=(BLUE, PURPLE))
        subtitle = Text("Episode 1: Money as Stored Work", font_size=32, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        channel = Text("Manan", font_size=40, color=GOLD).to_edge(UP)
        
        self.play(Write(channel), run_time=1)
        self.wait(0.5)
        self.play(
            FadeIn(title, shift=UP),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(FadeIn(subtitle, shift=UP), run_time=1)
        self.wait(2)
        
        # Transition: Conservation of Energy hint
        conservation = Text("Conservation of Energy", font_size=36, color=YELLOW)
        self.play(
            FadeOut(title, shift=UP),
            FadeOut(subtitle, shift=UP),
            FadeOut(channel, shift=UP)
        )
        self.play(Write(conservation), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(conservation))

    def scene_intrinsic_value(self):
        # Question appears
        question = Text("Does money have intrinsic value?", font_size=44, color=WHITE)
        self.play(Write(question), run_time=2)
        self.wait(2)
        
        # Show various forms of money
        self.play(question.animate.scale(0.7).to_edge(UP))
        
        # Create money symbols
        gold = Circle(radius=0.4, color=GOLD, fill_opacity=0.8).shift(LEFT*3)
        gold_label = Text("Gold", font_size=24).next_to(gold, DOWN)
        
        coin = Circle(radius=0.35, color=GRAY, fill_opacity=0.8).shift(LEFT*1)
        coin_label = Text("Coin", font_size=24).next_to(coin, DOWN)
        
        paper = Rectangle(width=1.2, height=0.6, color=GREEN, fill_opacity=0.8).shift(RIGHT*1)
        paper_label = Text("Paper", font_size=24).next_to(paper, DOWN)
        
        digital = Square(side_length=0.8, color=BLUE, fill_opacity=0.8).shift(RIGHT*3)
        digital_label = Text("Digital", font_size=24).next_to(digital, DOWN)
        
        money_group = VGroup(gold, gold_label, coin, coin_label, paper, paper_label, digital, digital_label)
        
        self.play(LaggedStart(*[FadeIn(obj, shift=UP) for obj in money_group], lag_ratio=0.2), run_time=2)
        self.wait(2)
        
        # Transform to "claim check" concept
        claim_text = Text("Money = Claim Check on Work", font_size=40, color=YELLOW)
        claim_text.move_to(ORIGIN)
        
        self.play(
            FadeOut(money_group),
            FadeOut(question),
            run_time=1
        )
        self.play(Write(claim_text), run_time=2)
        self.wait(2)
        self.play(FadeOut(claim_text))

    def scene_work_energy(self):
        # Show work examples
        title = Text("Real Physical Processes", font_size=42, color=BLUE_C).to_edge(UP)
        self.play(Write(title), run_time=1.5)
        
        # Three examples with icons
        farmer_icon = Circle(radius=0.5, color=GREEN, fill_opacity=0.6).shift(LEFT*4 + UP*0.5)
        farmer_text = Text("Farmer\nGrows Grain", font_size=24).next_to(farmer_icon, DOWN)
        
        factory_icon = Square(side_length=1, color=ORANGE, fill_opacity=0.6).shift(ORIGIN + UP*0.5)
        factory_text = Text("Factory\nAssembles Phone", font_size=24).next_to(factory_icon, DOWN)
        
        doctor_icon = Circle(radius=0.5, color=RED, fill_opacity=0.6).shift(RIGHT*4 + UP*0.5)
        doctor_text = Text("Doctor\nTreats Patient", font_size=24).next_to(doctor_icon, DOWN)
        
        examples = VGroup(farmer_icon, farmer_text, factory_icon, factory_text, doctor_icon, doctor_text)
        
        self.play(LaggedStart(*[FadeIn(obj, scale=0.5) for obj in examples], lag_ratio=0.3), run_time=2.5)
        self.wait(2)
        
        # Energy flow arrows
        arrow1 = Arrow(farmer_icon.get_bottom(), farmer_icon.get_bottom() + DOWN*1.5, color=YELLOW, buff=0.1)
        arrow2 = Arrow(factory_icon.get_bottom(), factory_icon.get_bottom() + DOWN*1.5, color=YELLOW, buff=0.1)
        arrow3 = Arrow(doctor_icon.get_bottom(), doctor_icon.get_bottom() + DOWN*1.5, color=YELLOW, buff=0.1)
        
        energy_label = Text("Energy + Labor → Value", font_size=32, color=YELLOW).next_to(arrow2, DOWN, buff=0.3)
        
        self.play(
            Create(arrow1),
            Create(arrow2),
            Create(arrow3),
            run_time=1.5
        )
        self.play(Write(energy_label), run_time=1.5)
        self.wait(2)
        
        self.play(
            FadeOut(VGroup(examples, arrow1, arrow2, arrow3, energy_label, title))
        )

    def scene_arithmetic_setup(self):
        # The key arithmetic example
        title = Text("Simple Arithmetic Example", font_size=42, color=GREEN).to_edge(UP)
        self.play(Write(title), run_time=1.5)
        
        # Initial state
        goods_label = Text("Goods Produced:", font_size=36).shift(UP*2 + LEFT*3)
        goods_value = Text("100 units", font_size=36, color=GREEN).next_to(goods_label, RIGHT)
        
        money_label = Text("Money Supply:", font_size=36).shift(UP*0.5 + LEFT*3)
        money_value = Text("100 claim checks", font_size=36, color=BLUE).next_to(money_label, RIGHT)
        
        self.play(
            Write(goods_label),
            Write(goods_value),
            run_time=1.5
        )
        self.wait(1)
        self.play(
            Write(money_label),
            Write(money_value),
            run_time=1.5
        )
        self.wait(1.5)
        
        # Division formula
        division_line = Line(LEFT*2, RIGHT*2, color=WHITE).shift(DOWN*1)
        numerator = Text("100 goods", font_size=32).next_to(division_line, UP, buff=0.3)
        denominator = Text("100 claim checks", font_size=32).next_to(division_line, DOWN, buff=0.3)
        equals = Text("=", font_size=40).next_to(division_line, RIGHT, buff=0.5)
        result = Text("1", font_size=40, color=YELLOW).next_to(equals, RIGHT, buff=0.3)
        
        formula_group = VGroup(division_line, numerator, denominator, equals, result)
        
        self.play(Create(formula_group), run_time=2)
        self.wait(1.5)
        
        explanation = Text("Each claim check buys 1 unit of goods", font_size=28, color=YELLOW)
        explanation.next_to(formula_group, DOWN, buff=0.8)
        
        self.play(Write(explanation), run_time=2)
        self.wait(2)
        
        self.play(FadeOut(VGroup(goods_label, goods_value, money_label, money_value, formula_group, explanation, title)))

    def scene_inflation_demo(self):
        # Show inflation effect
        title = Text("Printing More Money", font_size=42, color=RED).to_edge(UP)
        self.play(Write(title), run_time=1.5)
        
        # New state
        goods_label = Text("Goods Produced:", font_size=36).shift(UP*2 + LEFT*3)
        goods_value = Text("100 units", font_size=36, color=GREEN).next_to(goods_label, RIGHT)
        goods_note = Text("(unchanged)", font_size=24, color=GRAY).next_to(goods_value, RIGHT, buff=0.2)
        
        money_label = Text("Money Supply:", font_size=36).shift(UP*0.5 + LEFT*3)
        money_value_old = Text("100", font_size=36, color=BLUE).next_to(money_label, RIGHT)
        arrow = Text("→", font_size=36).next_to(money_value_old, RIGHT, buff=0.2)
        money_value_new = Text("200 claim checks", font_size=36, color=RED).next_to(arrow, RIGHT, buff=0.2)
        
        self.play(
            Write(goods_label),
            Write(goods_value),
            Write(goods_note),
            run_time=1.5
        )
        self.wait(1)
        self.play(
            Write(money_label),
            Write(money_value_old),
            run_time=1
        )
        self.play(
            Write(arrow),
            Write(money_value_new),
            run_time=1.5
        )
        self.wait(1.5)
        
        # New division
        division_line = Line(LEFT*2, RIGHT*2, color=WHITE).shift(DOWN*1)
        numerator = Text("100 goods", font_size=32).next_to(division_line, UP, buff=0.3)
        denominator = Text("200 claim checks", font_size=32, color=RED).next_to(division_line, DOWN, buff=0.3)
        equals = Text("=", font_size=40).next_to(division_line, RIGHT, buff=0.5)
        result = Text("0.5", font_size=40, color=ORANGE).next_to(equals, RIGHT, buff=0.3)
        
        formula_group = VGroup(division_line, numerator, denominator, equals, result)
        
        self.play(Create(formula_group), run_time=2)
        self.wait(1.5)
        
        explanation = Text("Each claim check now buys only 0.5 units", font_size=28, color=ORANGE)
        explanation.next_to(formula_group, DOWN, buff=0.8)
        
        inflation_box = Text("= INFLATION", font_size=36, color=RED, weight=BOLD)
        inflation_box.next_to(explanation, DOWN, buff=0.5)
        
        self.play(Write(explanation), run_time=2)
        self.wait(1)
        self.play(Write(inflation_box), run_time=1.5)
        self.wait(2.5)
        
        self.play(FadeOut(VGroup(goods_label, goods_value, goods_note, money_label, money_value_old, arrow, money_value_new, formula_group, explanation, inflation_box, title)))

    def scene_tickets_analogy(self):
        # Ticket analogy
        title = Text("The Ticket Analogy", font_size=42, color=PURPLE).to_edge(UP)
        self.play(Write(title), run_time=1.5)
        
        # Show seats
        seats = VGroup(*[Square(side_length=0.5, color=BLUE, fill_opacity=0.3) for _ in range(10)])
        seats.arrange(RIGHT, buff=0.2).shift(UP*1.5)
        seats_label = Text("10 Fixed Seats", font_size=28).next_to(seats, UP, buff=0.3)
        
        self.play(
            Create(seats),
            Write(seats_label),
            run_time=2
        )
        self.wait(1.5)
        
        # Show tickets scenario 1
        tickets1 = VGroup(*[Rectangle(width=0.4, height=0.6, color=GREEN, fill_opacity=0.6) for _ in range(10)])
        tickets1.arrange(RIGHT, buff=0.15).shift(DOWN*0.5)
        tickets1_label = Text("10 Tickets", font_size=28, color=GREEN).next_to(tickets1, DOWN, buff=0.3)
        
        self.play(
            Create(tickets1),
            Write(tickets1_label),
            run_time=1.5
        )
        self.wait(1)
        
        check1 = Text("✓ 1 ticket = 1 seat", font_size=28, color=GREEN).shift(DOWN*2.2)
        self.play(Write(check1), run_time=1)
        self.wait(2)
        
        # Show tickets scenario 2
        self.play(FadeOut(VGroup(tickets1, tickets1_label, check1)))
        
        tickets2 = VGroup(*[Rectangle(width=0.4, height=0.6, color=RED, fill_opacity=0.6) for _ in range(20)])
        tickets2.arrange(RIGHT, buff=0.1).shift(DOWN*0.5)
        tickets2_label = Text("20 Tickets", font_size=28, color=RED).next_to(tickets2, DOWN, buff=0.3)
        
        self.play(
            Create(tickets2),
            Write(tickets2_label),
            run_time=1.5
        )
        self.wait(1)
        
        check2 = Text("✗ Each ticket = weaker claim", font_size=28, color=RED).shift(DOWN*2.2)
        self.play(Write(check2), run_time=1)
        self.wait(2.5)
        
        self.play(FadeOut(VGroup(seats, seats_label, tickets2, tickets2_label, check2, title)))

    def scene_real_value_sources(self):
        # Sources of real value
        title = Text("Sources of Real Value", font_size=42, color=TEAL).to_edge(UP)
        self.play(Write(title), run_time=1.5)
        
        # Four pillars
        labor = Rectangle(width=1.5, height=2, color=BLUE, fill_opacity=0.4).shift(LEFT*4.5 + DOWN*0.5)
        labor_text = Text("Labor", font_size=28).move_to(labor)
        
        energy = Rectangle(width=1.5, height=2, color=YELLOW, fill_opacity=0.4).shift(LEFT*1.5 + DOWN*0.5)
        energy_text = Text("Energy", font_size=28).move_to(energy)
        
        resources = Rectangle(width=1.5, height=2, color=GREEN, fill_opacity=0.4).shift(RIGHT*1.5 + DOWN*0.5)
        resources_text = Text("Natural\nResources", font_size=24).move_to(resources)
        
        tech = Rectangle(width=1.5, height=2, color=PURPLE, fill_opacity=0.4).shift(RIGHT*4.5 + DOWN*0.5)
        tech_text = Text("Technology", font_size=28).move_to(tech)
        
        pillars = VGroup(labor, labor_text, energy, energy_text, resources, resources_text, tech, tech_text)
        
        self.play(LaggedStart(*[FadeIn(obj, shift=UP) for obj in pillars], lag_ratio=0.2), run_time=3)
        self.wait(2)
        
        # Arrow showing transformation
        transform_arrow = Arrow(UP*0.5, DOWN*2, color=ORANGE, buff=0.5, stroke_width=8)
        transform_text = Text("Transform into →", font_size=32, color=ORANGE).next_to(transform_arrow, RIGHT, buff=0.3)
        
        output = Text("Goods & Services", font_size=36, color=GOLD, weight=BOLD).shift(DOWN*3)
        
        self.play(
            Create(transform_arrow),
            Write(transform_text),
            run_time=1.5
        )
        self.play(Write(output), run_time=1.5)
        self.wait(2.5)
        
        self.play(FadeOut(VGroup(pillars, transform_arrow, transform_text, output, title)))

    def scene_production_effects(self):
        # Show production changes
        title = Text("Effect of Production Changes", font_size=42, color=BLUE_C).to_edge(UP)
        self.play(Write(title), run_time=1.5)
        
        # Scenario 1: Production increases
        scenario1 = Text("Scenario 1: Production Increases", font_size=32, color=GREEN).shift(UP*2)
        self.play(Write(scenario1), run_time=1.5)
        
        prod_up = VGroup(
            Text("More factories", font_size=26),
            Text("Better technology", font_size=26),
            Text("Higher productivity", font_size=26)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP*0.5 + LEFT*3)
        
        arrow1 = Arrow(LEFT*0.5, RIGHT*0.5, color=GREEN).shift(UP*0.5)
        result1 = Text("Prices ↓\n(or stable)", font_size=28, color=GREEN).next_to(arrow1, RIGHT, buff=0.5)
        
        self.play(Write(prod_up), run_time=2)
        self.play(Create(arrow1), Write(result1), run_time=1.5)
        self.wait(2)
        
        self.play(FadeOut(VGroup(scenario1, prod_up, arrow1, result1)))
        
        # Scenario 2: Production decreases
        scenario2 = Text("Scenario 2: Production Decreases", font_size=32, color=RED).shift(UP*2)
        self.play(Write(scenario2), run_time=1.5)
        
        prod_down = VGroup(
            Text("Energy crisis", font_size=26),
            Text("Supply chain disruption", font_size=26),
            Text("Natural disasters", font_size=26)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP*0.5 + LEFT*3)
        
        arrow2 = Arrow(LEFT*0.5, RIGHT*0.5, color=RED).shift(UP*0.5)
        result2 = Text("Prices ↑\n(Inflation)", font_size=28, color=RED).next_to(arrow2, RIGHT, buff=0.5)
        
        self.play(Write(prod_down), run_time=2)
        self.play(Create(arrow2), Write(result2), run_time=1.5)
        self.wait(2.5)
        
        self.play(FadeOut(VGroup(scenario2, prod_down, arrow2, result2, title)))

    def scene_monetary_policy(self):
        # Monetary policy discussion
        title = Text("Role of Monetary Policy", font_size=42, color=GOLD).to_edge(UP)
        self.play(Write(title), run_time=1.5)
        
        # Two paths
        path1_title = Text("With Productive Investment", font_size=30, color=GREEN).shift(UP*2 + LEFT*3)
        path2_title = Text("Without Productive Investment", font_size=30, color=RED).shift(UP*2 + RIGHT*3)
        
        self.play(
            Write(path1_title),
            Write(path2_title),
            run_time=2
        )
        self.wait(1)
        
        # Path 1
        money_exp1 = Text("Money ↑", font_size=24, color=BLUE).shift(UP*0.8 + LEFT*3)
        plus1 = Text("+", font_size=28).shift(UP*0.2 + LEFT*3)
        prod_inv1 = Text("Production ↑", font_size=24, color=GREEN).shift(DOWN*0.4 + LEFT*3)
        equals1 = Text("=", font_size=28).shift(DOWN*1.2 + LEFT*3)
        result1 = Text("Stable Prices", font_size=24, color=GREEN, weight=BOLD).shift(DOWN*2 + LEFT*3)
        
        path1 = VGroup(money_exp1, plus1, prod_inv1, equals1, result1)
        
        # Path 2
        money_exp2 = Text("Money ↑", font_size=24, color=BLUE).shift(UP*0.8 + RIGHT*3)
        plus2 = Text("+", font_size=28).shift(UP*0.2 + RIGHT*3)
        prod_inv2 = Text("Production →", font_size=24, color=GRAY).shift(DOWN*0.4 + RIGHT*3)
        equals2 = Text("=", font_size=28).shift(DOWN*1.2 + RIGHT*3)
        result2 = Text("Inflation", font_size=24, color=RED, weight=BOLD).shift(DOWN*2 + RIGHT*3)
        
        path2 = VGroup(money_exp2, plus2, prod_inv2, equals2, result2)
        
        self.play(LaggedStart(Write(path1), Write(path2), lag_ratio=0.5), run_time=3)
        self.wait(3)
        
        self.play(FadeOut(VGroup(path1_title, path2_title, path1, path2, title)))

    def scene_physical_limits(self):
        # Physical constraints
        title = Text("Physical Limits to Growth", font_size=42, color=RED_C).to_edge(UP)
        self.play(Write(title), run_time=1.5)
        
        # Entropy concept
        low_entropy = Rectangle(width=2, height=1.5, color=BLUE, fill_opacity=0.7).shift(LEFT*4 + UP*0.5)
        low_text = Text("Low Entropy\nResources", font_size=24, color=WHITE).move_to(low_entropy)
        
        process_arrow = Arrow(LEFT*2.5, RIGHT*2.5, color=YELLOW, buff=0, stroke_width=10)
        process_label = Text("Economic\nProcesses", font_size=24, color=YELLOW).next_to(process_arrow, UP, buff=0.2)
        
        high_entropy = Rectangle(width=2, height=1.5, color=RED, fill_opacity=0.7).shift(RIGHT*4 + UP*0.5)
        high_text = Text("High Entropy\nWaste", font_size=24, color=WHITE).move_to(high_entropy)
        
        entropy_group = VGroup(low_entropy, low_text, process_arrow, process_label, high_entropy, high_text)
        
        self.play(LaggedStart(
            FadeIn(VGroup(low_entropy, low_text)),
            Create(process_arrow),
            Write(process_label),
            FadeIn(VGroup(high_entropy, high_text)),
            lag_ratio=0.4
        ), run_time=3)
        self.wait(2)
        
        # Constraint message
        constraint = Text("Physical laws impose real constraints", font_size=32, color=ORANGE)
        constraint.shift(DOWN*2)
        
        self.play(Write(constraint), run_time=2)
        self.wait(2.5)
        
        self.play(FadeOut(VGroup(entropy_group, constraint, title)))

    def scene_summary(self):
        # Summary of key points
        title = Text("Key Takeaways", font_size=48, color=GOLD, weight=BOLD).to_edge(UP)
        self.play(Write(title), run_time=1.5)
        self.wait(1)
        
        points = VGroup(
            Text("1. Money = Claim Check on Stored Work", font_size=30, color=BLUE),
            Text("2. More Money + Same Goods = Inflation", font_size=30, color=RED),
            Text("3. Real Growth = Expanding Productive Capacity", font_size=30, color=GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.8).shift(DOWN*0.5)
        
        # Animate each point
        for i, point in enumerate(points):
            self.play(Write(point), run_time=2)
            self.wait(1.5)
        
        self.wait(2)
        self.play(FadeOut(VGroup(points, title)))

    def scene_next_episode(self):
        # Next episode teaser
        coming_next = Text("Coming Next...", font_size=40, color=PURPLE).shift(UP*2)
        self.play(Write(coming_next), run_time=1.5)
        self.wait(1)
        
        episode2 = Text("Episode 2:", font_size=36, weight=BOLD).shift(UP*0.5)
        subtitle = Text("The Fluid Dynamics of Cash Flow", font_size=32, color=BLUE)
        subtitle.next_to(episode2, DOWN, buff=0.5)
        
        formula = MathTex("MV = PQ", font_size=72, color=YELLOW).shift(DOWN*1.5)
        
        self.play(
            Write(episode2),
            Write(subtitle),
            run_time=2
        )
        self.wait(1)
        self.play(Write(formula), run_time=2)
        self.wait(2)
        
        # Call to action
        cta = Text("Subscribe for more episodes!", font_size=32, color=GREEN).shift(DOWN*3)
        self.play(Write(cta), run_time=1.5)
        self.wait(3)
        
        # Final fadeout
        self.play(FadeOut(VGroup(coming_next, episode2, subtitle, formula, cta)), run_time=2)
        self.wait(1)
