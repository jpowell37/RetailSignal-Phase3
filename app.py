
import streamlit as st

from sample_data import sample_products

st.set_page_config(
    page_title="RetailSignal",
    page_icon="📊",
    layout="wide"
)

st.caption(
    "Academic prototype | Product costs, market assumptions, "
    "demand-test results, and recommendations are illustrative "
    "unless independently verified."
)

st.markdown(
    """
    <style>

    .stApp {
        background-color: #F8F6F1;
    }

h1 {
    color: #17324D !important;
    font-weight: 750 !important;
    letter-spacing: -1px;
}

    /* Main website layout */
    .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Main headings */
    h1 {
        font-weight: 750;
        letter-spacing: -1px;
    }

    h2, h3 {
        font-weight: 650;
        letter-spacing: -0.3px;
    }

    /* Primary action buttons */
    div.stButton > button {
        
background-color: #17324D !important;

        color: #FFFFFF;
        border: 1px solid #17324D;
        border-radius: 10px;
        font-weight: 600;
        padding: 0.65rem 1.25rem;
    }

    div.stButton > button[kind="primary"]:hover {
        background-color: #247C87;
        border-color: #247C87;
        color: #FFFFFF;
    }

    /* Form controls */
    div[data-testid="stTextInput"] input,
    div[data-testid="stNumberInput"] input {
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if "page" not in st.session_state:
    st.session_state["page"] = "home"

if st.session_state["page"] == "home":

    st.title("RetailSignal")

    

    st.write(
        "Discover promising products, evaluate financial feasibility, "
        "and make informed investment decisions before committing capital."
    )

    
    
    # ============================================
    # RETAILSIGNAL - LUXURY FINTECH HOMEPAGE
    # ============================================

    st.markdown(
        "".join([
            '<div style="background:linear-gradient(135deg,#FFFFFF,#EEF7F4);'
            'border:1px solid #DCE8E3;border-radius:24px;'
            'padding:60px 30px;text-align:center;'
            'box-shadow:0 12px 35px rgba(23,50,77,0.06);'
            'margin:20px 0 25px 0;">',

            '<div style="color:#247C87;font-size:12px;'
            'font-weight:700;letter-spacing:3px;'
            'margin-bottom:20px;">'
            'RETAILSIGNAL | COMMERCE INTELLIGENCE'
            '</div>',

            '<div style="color:#17324D;font-size:44px;'
            'font-weight:800;line-height:1.2;'
            'margin-bottom:18px;">'
            'Know the opportunity.'
            '<div style="color:#247C87;">'
            'Understand the risk.'
            '</div>'
            '</div>',

            '<div style="color:#64748B;font-size:17px;'
            'line-height:1.7;max-width:680px;'
            'margin:0 auto 25px auto;">'
            'Discover potential e-commerce opportunities, '
            'evaluate financial feasibility, compare supplier '
            'commitments, and validate customer demand '
            'before investing.'
            '</div>',

            '<div style="background:#C5A46D;width:75px;'
            'height:3px;border-radius:10px;'
            'margin:25px auto;"></div>',

            '<div style="color:#17324D;font-size:16px;'
            'font-weight:600;">'
            'Choose how to begin your analysis'
            '</div>',

            '</div>'
        ]),
        unsafe_allow_html=True,
    )

    # ============================================
    # NAVIGATION BUTTONS
    # ============================================

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        if st.button(
            "Discover Opportunities",
            use_container_width=True,
            key="home_discover",
        ):
            st.session_state["page"] = "discover"
            st.rerun()

    with col2:
        if st.button(
            "Evaluate My Idea",
            use_container_width=True,
            key="home_evaluate",
        ):
            st.session_state["page"] = "evaluate"
            st.rerun()

    # ============================================
    # PLATFORM FEATURES
    # ============================================

    st.markdown(
        "".join([
            '<div style="text-align:center;'
            'padding:45px 10px 25px;">',

            '<div style="color:#247C87;font-size:12px;'
            'font-weight:700;letter-spacing:2px;">'
            'THE RETAILSIGNAL ADVANTAGE'
            '</div>',

            '<div style="color:#17324D;font-size:29px;'
            'font-weight:750;margin-top:12px;">'
            'Intelligence for better business decisions'
            '</div>',

            '<div style="color:#64748B;font-size:15px;'
            'margin-top:12px;">'
            'A structured approach to discovering, '
            'analyzing, and validating product opportunities.'
            '</div>',

            '</div>'
        ]),
        unsafe_allow_html=True,
    )

    
    # THREE PLATFORM FEATURE CARDS

    feature_col1, feature_col2, feature_col3 = st.columns(3, gap="medium")

    with feature_col1:
        with st.container(border=True):
            st.caption("01 / DISCOVER")
            st.markdown("### Market Opportunities")
            st.write(
                "Explore illustrative product opportunities "
                "based on your business goals and available capital."
            )

    with feature_col2:
        with st.container(border=True):
            st.caption("02 / ANALYZE")
            st.markdown("### Financial Intelligence")
            st.write(
                "Compare supplier commitments, contribution "
                "margins, and startup capital requirements."
            )

    with feature_col3:
        with st.container(border=True):
            st.caption("03 / VALIDATE")
            st.markdown("### Investment Readiness")
            st.write(
                "Review demand-test evidence, identify "
                "potential risks, and explore recommended next steps."
            )


    # ============================================
    # PROTOTYPE NOTICE
    # ============================================

    st.markdown(
        "".join([
            '<div style="text-align:center;'
            'padding:30px 15px;'
            'color:#7A8794;font-size:12px;">'
            'Academic prototype | Illustrative data '
            'and rule-based recommendations. '
            'Not financial or investment advice.'
            '</div>'
        ]),
        unsafe_allow_html=True,
    )



    

    

    





    

           


         




# ==========================================================
# RETAILSIGNAL — DISCOVER OPPORTUNITIES DASHBOARD
# ==========================================================

if st.session_state.get("page") == "discover":

    st.markdown(
        '<div style="color:#247C87;font-size:12px;'
        'font-weight:700;letter-spacing:2px;">'
        'RETAILSIGNAL / MARKET INTELLIGENCE</div>',
        unsafe_allow_html=True,
    )

    st.title("Discover Opportunities")

    st.write(
        "Explore potential e-commerce products, assess startup "
        "requirements, and review financial and demand evidence "
        "before committing capital."
    )

    st.divider()

    # ------------------------------------------------------
    # ENTREPRENEUR DISCOVERY ASSESSMENT
    # ------------------------------------------------------

    st.subheader("Your Business Profile")

    st.caption(
        "Start with your interests, available capital, "
        "and primary business objective."
    )

    with st.container(border=True):

        profile_col1, profile_col2 = st.columns(2)

        with profile_col1:
            interest = st.selectbox(
                "Product Category",
                [
                    "Select a category",
                    "Beauty & Personal Care",
                    "Fashion & Accessories",
                    "Home & Lifestyle",
                    "Other Consumer Products",
                ],
                key="discover_interest",
            )

        with profile_col2:
            capital = st.number_input(
                "Available Startup Capital ($)",
                min_value=0.0,
                value=1500.0,
                step=100.0,
                format="%.2f",
                key="discover_capital",
            )

        goal = st.selectbox(
            "Primary Business Goal",
            [
                "Select a goal",
                "Discover a promising product opportunity",
                "Validate demand before investing",
                "Launch a small e-commerce business",
                "Evaluate an existing product idea",
            ],
            key="discover_goal",
        )

        analyze = st.button(
            "Analyze Opportunities",
            type="primary",
            use_container_width=True,
            key="discover_analyze",
        )

    # ------------------------------------------------------
    # OPPORTUNITY RESULTS
    # ------------------------------------------------------

    if analyze:

        if (
            interest == "Select a category"
            or goal == "Select a goal"
        ):
            st.warning(
                "Please select a product category and business goal."
            )

        else:

            matching_products = [
                product
                for product in sample_products
                if product["category"] == interest
            ]

            st.divider()

            st.markdown(
                '<div style="color:#247C87;font-size:12px;'
                'font-weight:700;letter-spacing:2px;">'
                'OPPORTUNITY INTELLIGENCE</div>',
                unsafe_allow_html=True,
            )

            st.subheader("Your Product Opportunities")

            st.caption(
                "Results use illustrative product data and "
                "preliminary rule-based assessments."
            )

            if not matching_products:
                st.info(
                    "No sample products are currently available "
                    "for this category."
                )

            for product in matching_products:

                product_name = product["product"]

                unit_cost = product["estimated_unit_cost"]

                moq = product["minimum_order_quantity"]

                packaging_unit = product.get(
                    "packaging_cost_per_unit", 0
                )

                selling_price = product.get(
                    "estimated_selling_price"
                )

                other_variable_cost = product.get(
                    "other_variable_cost_per_sale", 0
                )

                test_visitors = product.get("test_visitors")

                test_paid_orders = product.get(
                    "test_paid_orders"
                )

                test_spend = product.get("test_spend")

                # ------------------------------------------
                # FINANCIAL CALCULATIONS
                # ------------------------------------------

                inventory_cost = unit_cost * moq

                packaging_cost = packaging_unit * moq

                initial_commitment = (
                    inventory_cost + packaging_cost
                )

                remaining_capital = (
                    capital - initial_commitment
                )

                if selling_price is not None:

                    variable_cost = (
                        unit_cost
                        + packaging_unit
                        + other_variable_cost
                    )

                    contribution_margin = (
                        selling_price - variable_cost
                    )

                    if selling_price > 0:
                        margin_ratio = (
                            contribution_margin
                            / selling_price
                        ) * 100
                    else:
                        margin_ratio = None

                else:
                    variable_cost = None
                    contribution_margin = None
                    margin_ratio = None

                if (
                    test_visitors is not None
                    and test_paid_orders is not None
                    and test_visitors > 0
                ):
                    conversion_rate = (
                        test_paid_orders / test_visitors
                    ) * 100
                else:
                    conversion_rate = None

                # ------------------------------------------
                # PRODUCT OVERVIEW
                # ------------------------------------------

                with st.container(border=True):

                    st.caption("PRODUCT OPPORTUNITY")

                    st.subheader(product_name)

                    st.write(
                        f"**Category:** {product['category']}"
                    )

                    st.divider()

                    st.markdown("#### Financial Overview")

                    metric1, metric2, metric3 = st.columns(3)

                    with metric1:
                        st.metric(
                            "Initial Commitment",
                            f"${initial_commitment:,.2f}",
                        )

                    with metric2:
                        st.metric(
                            "Capital Remaining",
                            f"${remaining_capital:,.2f}",
                        )

                    with metric3:
                        st.metric(
                            "Minimum Order",
                            f"{moq:,} units",
                        )

                    st.markdown("#### Capital Utilization")

                    if capital > 0:

                        utilization = (
                            initial_commitment / capital
                        ) * 100

                        st.progress(
                            min(utilization / 100, 1.0)
                        )

                        st.caption(
                            f"{utilization:.1f}% of available "
                            "startup capital would be committed "
                            "to initial inventory and packaging."
                        )

                    else:
                        st.warning(
                            "Capital utilization cannot be "
                            "calculated with $0 startup capital."
                        )

                    st.divider()

                    # --------------------------------------
                    # COST BREAKDOWN
                    # --------------------------------------

                    st.markdown("#### Product Cost Analysis")

                    cost_col1, cost_col2 = st.columns(2)

                    with cost_col1:
                        st.write(
                            f"**Supplier Cost per Unit:** "
                            f"${unit_cost:,.2f}"
                        )

                        st.write(
                            f"**Inventory Cost:** "
                            f"${inventory_cost:,.2f}"
                        )

                    with cost_col2:
                        st.write(
                            f"**Packaging per Unit:** "
                            f"${packaging_unit:,.2f}"
                        )

                        st.write(
                            f"**Total Packaging Cost:** "
                            f"${packaging_cost:,.2f}"
                        )

                    if selling_price is not None:

                        st.divider()

                        st.markdown(
                            "#### Profitability Indicators"
                        )

                        profit_col1, profit_col2 = st.columns(2)

                        with profit_col1:
                            st.metric(
                                "Proposed Selling Price",
                                f"${selling_price:,.2f}",
                            )

                        with profit_col2:
                            st.metric(
                                "Contribution Margin / Sale",
                                f"${contribution_margin:,.2f}",
                            )

                        st.write(
                            f"**Variable Expenses per Sale:** "
                            f"${variable_cost:,.2f}"
                        )

                        if margin_ratio is not None:
                            st.write(
                                f"**Contribution Margin Ratio:** "
                                f"{margin_ratio:.1f}%"
                            )
                        else:
                            st.warning(
                                "A selling price above $0 is "
                                "required to calculate the margin ratio."
                            )

                        st.caption(
                            "Contribution margin excludes fixed "
                            "expenses and does not guarantee profit."
                        )

                    else:
                        st.warning(
                            "INSUFFICIENT DATA — A proposed selling "
                            "price is needed for profitability analysis."
                        )

                    st.divider()

                    # --------------------------------------
                    # DEMAND VALIDATION
                    # --------------------------------------

                    st.markdown("#### Demand Validation")

                    if conversion_rate is not None:

                        demand1, demand2, demand3 = st.columns(3)

                        with demand1:
                            st.metric(
                                "Test Visitors",
                                f"{test_visitors:,}",
                            )

                        with demand2:
                            st.metric(
                                "Paid Orders",
                                f"{test_paid_orders:,}",
                            )

                        with demand3:
                            st.metric(
                                "Conversion Rate",
                                f"{conversion_rate:.1f}%",
                            )

                        if test_spend is not None:
                            st.caption(
                                f"Reported demand-test spending: "
                                f"${test_spend:,.2f}"
                            )

                    else:
                        st.warning(
                            "INSUFFICIENT DATA — Usable demand-test "
                            "results are not available."
                        )

                    st.divider()

                    # --------------------------------------
                    # INVESTMENT READINESS ASSESSMENT
                    # --------------------------------------

                    st.caption(
                        "RETAILSIGNAL | OPPORTUNITY DECISION"
                    )

                    st.subheader(
                        "Investment Readiness Assessment"
                    )

                    risk_reasons = []

                    if remaining_capital < 0:
                        risk_reasons.append(
                            "The initial inventory and packaging "
                            "commitment exceeds available capital."
                        )

                    if contribution_margin is not None:
                        if contribution_margin <= 0:
                            risk_reasons.append(
                                "Estimated variable expenses equal "
                                "or exceed the selling price."
                            )

                    if (
                        conversion_rate is not None
                        and test_paid_orders == 0
                    ):
                        risk_reasons.append(
                            "The demand test reported no paid orders."
                        )

                    if risk_reasons:

                        st.error(
                            "NOT READY — Financial or demand risks "
                            "require attention before inventory investment."
                        )

                        st.markdown("**Identified Risk Factors**")

                        for reason in risk_reasons:
                            st.write(f"• {reason}")

                        st.markdown("**Recommended Next Action**")

                        st.write(
                            "Review costs, improve the product offer, "
                            "and conduct additional demand validation "
                            "before committing capital."
                        )

                    elif (
                        contribution_margin is None
                        or conversion_rate is None
                    ):

                        st.warning(
                            "INSUFFICIENT DATA — More pricing or "
                            "purchasing-demand evidence is needed."
                        )

                        st.write(
                            "**Recommended Next Action:** "
                            "Confirm the proposed selling price and "
                            "conduct a controlled demand test."
                        )

                    elif (
                        test_visitors >= 100
                        and test_paid_orders >= 10
                    ):

                        st.success(
                            "PROMISING — Preliminary financial "
                            "and illustrative demand criteria are met."
                        )

                        st.write(
                            "**Recommended Next Action:** "
                            "Verify supplier quotations and consider "
                            "a small controlled pilot."
                        )

                    else:

                        st.info(
                            "POTENTIAL — Some positive demand evidence "
                            "exists, but additional validation is needed."
                        )

                        st.write(
                            "**Recommended Next Action:** "
                            "Continue testing customer purchasing "
                            "interest before investing in inventory."
                        )

                    st.caption(
                        "Preliminary academic assessment using "
                        "illustrative assumptions. Results are not "
                        "a guarantee of business success."
                    )

    # ------------------------------------------------------
    # PAGE NAVIGATION
    # ------------------------------------------------------

    st.divider()

    if st.button(
        "Return to Home",
        key="discover_return_home",
    ):
        st.session_state["page"] = "home"
        st.rerun()

# ==========================================================
# END OF DISCOVER OPPORTUNITIES DASHBOARD
# ==========================================================








# ==========================================================
# RETAILSIGNAL | EVALUATE MY IDEA
# Financial Intelligence Dashboard
# ==========================================================

if st.session_state.get("page") == "evaluate":

    st.caption("RETAILSIGNAL  /  FINANCIAL INTELLIGENCE")
    st.title("Evaluate My Idea")

    st.write(
        "Turn your product idea into an evidence-based business "
        "decision. Compare sourcing commitments, analyze unit "
        "economics, and assess customer demand before investing."
    )

    st.divider()

    # ------------------------------------------------------
    # 01 | PRODUCT AND CAPITAL
    # ------------------------------------------------------

    st.subheader("01 / Product & Capital")

    with st.container(border=True):

        product_name = st.text_input(
            "Product Name",
            placeholder="Example: Hydrating Lip Oil",
            key="idea_product_name",
        )

        col1, col2 = st.columns(2)

        with col1:
            idea_capital = st.number_input(
                "Available Startup Capital ($)",
                min_value=0.0,
                value=1500.0,
                step=100.0,
                key="idea_capital",
            )

        with col2:
            idea_selling_price = st.number_input(
                "Proposed Selling Price ($)",
                min_value=0.0,
                value=18.0,
                step=1.0,
                key="idea_selling_price",
            )

    # ------------------------------------------------------
    # 02 | SUPPLIER INTELLIGENCE
    # ------------------------------------------------------

    st.subheader("02 / Supplier Intelligence")

    st.caption(
        "Compare two hypothetical sourcing scenarios. "
        "Supplier A is used for the main financial assessment."
    )

    supplier_a_col, supplier_b_col = st.columns(2)

    with supplier_a_col:

        with st.container(border=True):

            st.markdown("#### Supplier A")
            st.caption("Primary financial scenario")

            idea_supplier_cost = st.number_input(
                "Unit Cost ($)",
                min_value=0.0,
                value=4.50,
                step=0.50,
                key="idea_supplier_cost",
            )

            idea_moq = st.number_input(
                "Minimum Order Quantity",
                min_value=1,
                value=150,
                step=1,
                key="idea_moq",
            )

    with supplier_b_col:

        with st.container(border=True):

            st.markdown("#### Supplier B")
            st.caption("Alternative sourcing scenario")

            supplier_b_cost = st.number_input(
                "Unit Cost ($)",
                min_value=0.0,
                value=5.00,
                step=0.50,
                key="supplier_b_cost",
            )

            supplier_b_moq = st.number_input(
                "Minimum Order Quantity",
                min_value=1,
                value=100,
                step=1,
                key="supplier_b_moq",
            )

    # ------------------------------------------------------
    # 03 | ADDITIONAL COSTS
    # ------------------------------------------------------

    st.subheader("03 / Operating Cost Assumptions")

    with st.container(border=True):

        cost_col1, cost_col2 = st.columns(2)

        with cost_col1:
            idea_packaging_cost = st.number_input(
                "Packaging Cost per Unit ($)",
                min_value=0.0,
                value=1.75,
                step=0.25,
                key="idea_packaging_cost",
            )

        with cost_col2:
            idea_other_cost = st.number_input(
                "Other Variable Costs per Sale ($)",
                min_value=0.0,
                value=9.24,
                step=0.25,
                key="idea_other_cost",
            )

        st.caption(
            "Other variable costs may include estimated "
            "transaction fees, fulfillment, and marketing "
            "expenses attributable to each sale."
        )

    # ------------------------------------------------------
    # 04 | DEMAND VALIDATION
    # ------------------------------------------------------

    st.subheader("04 / Demand Validation")

    with st.container(border=True):

        st.write(
            "Enter results from a small customer demand test."
        )

        demand_col1, demand_col2 = st.columns(2)

        with demand_col1:
            idea_visitors = st.number_input(
                "Test Visitors",
                min_value=0,
                value=0,
                step=1,
                key="idea_visitors",
            )

        with demand_col2:
            idea_paid_orders = st.number_input(
                "Paid Orders",
                min_value=0,
                value=0,
                step=1,
                key="idea_paid_orders",
            )

        st.caption(
            "Use actual test observations when available. "
            "Hypothetical entries are for demonstration only."
        )

    st.divider()

    run_analysis = st.button(
        "Generate Financial Intelligence Report",
        type="primary",
        use_container_width=True,
        key="run_idea_analysis",
    )

    # ------------------------------------------------------
    # FINANCIAL INTELLIGENCE REPORT
    # ------------------------------------------------------

    if run_analysis:

        if not product_name.strip():
            st.warning(
                "Enter a product name before generating the report."
            )

        elif idea_paid_orders > idea_visitors:
            st.error(
                "Paid orders cannot exceed test visitors "
                "in this simplified conversion model."
            )

        elif idea_selling_price <= 0:
            st.warning(
                "Enter a selling price greater than $0."
            )

        else:

            # ----------------------------------------------
            # FINANCIAL CALCULATIONS
            # ----------------------------------------------

            idea_initial_cost = (
                idea_supplier_cost + idea_packaging_cost
            ) * idea_moq

            supplier_b_initial_cost = (
                supplier_b_cost + idea_packaging_cost
            ) * supplier_b_moq

            idea_remaining = (
                idea_capital - idea_initial_cost
            )

            idea_variable_cost = (
                idea_supplier_cost
                + idea_packaging_cost
                + idea_other_cost
            )

            idea_margin = (
                idea_selling_price - idea_variable_cost
            )

            margin_percentage = (
                idea_margin / idea_selling_price
            ) * 100

            if idea_visitors > 0:
                idea_conversion_rate = (
                    idea_paid_orders / idea_visitors
                ) * 100
            else:
                idea_conversion_rate = None

            # ----------------------------------------------
            # REPORT HEADER
            # ----------------------------------------------

            st.divider()

            st.caption(
                "RETAILSIGNAL  /  OPPORTUNITY ANALYSIS REPORT"
            )

            st.title("Financial Intelligence Report")
            st.write(f"**Product:** {product_name}")

            st.caption(
                "Preliminary assessment based on entered "
                "financial assumptions and demand evidence."
            )

            # ----------------------------------------------
            # EXECUTIVE FINANCIAL METRICS
            # ----------------------------------------------

            st.subheader("Financial Overview")

            metric1, metric2, metric3 = st.columns(3)

            with metric1:
                with st.container(border=True):
                    st.metric(
                        "Initial Commitment",
                        f"${idea_initial_cost:,.2f}",
                    )

            with metric2:
                with st.container(border=True):
                    st.metric(
                        "Capital Remaining",
                        f"${idea_remaining:,.2f}",
                    )

            with metric3:
                with st.container(border=True):
                    st.metric(
                        "Contribution Margin",
                        f"${idea_margin:,.2f}",
                    )

            st.markdown("#### Capital Utilization")

            if idea_capital > 0:

                utilization = (
                    idea_initial_cost / idea_capital
                ) * 100

                st.progress(
                    min(utilization / 100, 1.0)
                )

                st.caption(
                    f"{utilization:.1f}% of available startup "
                    "capital is required for initial inventory "
                    "and packaging."
                )

            else:
                st.warning(
                    "Capital utilization cannot be calculated "
                    "with $0 available capital."
                )

            # ----------------------------------------------
            # SUPPLIER COMPARISON
            # ----------------------------------------------

            st.divider()
            st.subheader("Supplier Comparison")

            supplier1, supplier2 = st.columns(2)

            with supplier1:

                with st.container(border=True):

                    st.markdown("#### Supplier A")

                    st.metric(
                        "Initial Commitment",
                        f"${idea_initial_cost:,.2f}",
                    )

                    st.write(
                        f"**Unit Cost:** "
                        f"${idea_supplier_cost:,.2f}"
                    )

                    st.write(
                        f"**Minimum Order:** "
                        f"{idea_moq:,} units"
                    )

            with supplier2:

                with st.container(border=True):

                    st.markdown("#### Supplier B")

                    st.metric(
                        "Initial Commitment",
                        f"${supplier_b_initial_cost:,.2f}",
                    )

                    st.write(
                        f"**Unit Cost:** "
                        f"${supplier_b_cost:,.2f}"
                    )

                    st.write(
                        f"**Minimum Order:** "
                        f"{supplier_b_moq:,} units"
                    )

            
            difference = abs(
                idea_initial_cost - supplier_b_initial_cost
            )

            


            difference = abs(
                idea_initial_cost - supplier_b_initial_cost
            )

            if supplier_b_initial_cost < idea_initial_cost:
                st.info(
                    f"Supplier B requires ${difference:,.2f} "
                    "less upfront capital. Compare unit costs "
                    "and order quantities before deciding."
                )

            elif idea_initial_cost < supplier_b_initial_cost:
                st.info(
                    f"Supplier A requires ${difference:,.2f} "
                    "less upfront capital. Review the total "
                    "commitment and unit-price tradeoffs."
                )

            else:
                st.info(
                    "Both suppliers require the same "
                    "estimated upfront commitment."
                )

            st.caption(
                "Both scenarios assume the same packaging cost. "
                "Supplier quotations have not been verified."
            )

            # ----------------------------------------------
            # UNIT ECONOMICS
            # ----------------------------------------------

            st.divider()
            st.subheader("Profitability Analysis")

            profit1, profit2 = st.columns(2)

            with profit1:
                with st.container(border=True):
                    st.metric(
                        "Variable Cost per Sale",
                        f"${idea_variable_cost:,.2f}",
                    )

            with profit2:
                with st.container(border=True):
                    st.metric(
                        "Contribution Margin Ratio",
                        f"{margin_percentage:.1f}%",
                    )

            st.caption(
                "Contribution margin is selling price minus "
                "estimated variable expenses. Fixed costs "
                "are not included."
            )

            # ----------------------------------------------
            # DEMAND VALIDATION DASHBOARD
            # ----------------------------------------------

            st.divider()
            st.subheader("Demand Validation Dashboard")

            if idea_conversion_rate is not None:

                demand1, demand2, demand3 = st.columns(3)

                with demand1:
                    st.metric(
                        "Test Visitors",
                        f"{idea_visitors:,}",
                    )

                with demand2:
                    st.metric(
                        "Paid Orders",
                        f"{idea_paid_orders:,}",
                    )

                with demand3:
                    st.metric(
                        "Conversion Rate",
                        f"{idea_conversion_rate:.1f}%",
                    )

                st.progress(
                    min(idea_conversion_rate / 100, 1.0)
                )

                st.caption(
                    "Observed paid-order conversion rate "
                    "within the entered demand-test sample."
                )

            else:

                st.warning(
                    "INSUFFICIENT DATA — No demand-test "
                    "visitors have been entered."
                )

            # ----------------------------------------------
            # INVESTMENT READINESS
            # ----------------------------------------------

            st.divider()

            st.caption(
                "RETAILSIGNAL  /  EXECUTIVE DECISION SUMMARY"
            )

            st.subheader("Investment Readiness Assessment")

            risk_reasons = []

            if idea_margin <= 0:
                risk_reasons.append(
                    "Estimated variable expenses equal or "
                    "exceed the proposed selling price."
                )

            if idea_remaining < 0:
                risk_reasons.append(
                    "Initial inventory and packaging costs "
                    "exceed available startup capital."
                )

            if (
                idea_conversion_rate is not None
                and idea_paid_orders == 0
            ):
                risk_reasons.append(
                    "The demand test generated no paid orders."
                )

            if risk_reasons:

                decision = "NOT READY"

                st.error(
                    "NOT READY — Financial or demand risks "
                    "must be addressed before investing."
                )

            elif idea_conversion_rate is None:

                decision = "INSUFFICIENT DATA"

                st.warning(
                    "INSUFFICIENT DATA — Customer purchasing "
                    "demand has not been established."
                )

            elif (
                idea_visitors >= 100
                and idea_paid_orders >= 10
            ):

                decision = "PROMISING"

                st.success(
                    "PROMISING — Preliminary financial "
                    "and illustrative demand criteria are met."
                )

            else:

                decision = "POTENTIAL"

                st.info(
                    "POTENTIAL — Positive demand evidence "
                    "exists, but more validation is recommended."
                )

            # ----------------------------------------------
            # DECISION RATIONALE
            # ----------------------------------------------

            with st.container(border=True):

                st.markdown("#### Supporting Evidence")

                st.write(
                    f"**Financial:** Contribution margin is "
                    f"${idea_margin:,.2f} per sale. "
                    f"Remaining capital is "
                    f"${idea_remaining:,.2f}."
                )

                if idea_conversion_rate is not None:

                    st.write(
                        f"**Demand:** {idea_paid_orders:,} "
                        f"paid orders from {idea_visitors:,} "
                        f"visitors, representing a "
                        f"{idea_conversion_rate:.1f}% "
                        "observed conversion rate."
                    )

                else:

                    st.write(
                        "**Demand:** Insufficient purchasing "
                        "evidence is available."
                    )

                if risk_reasons:

                    st.markdown("#### Identified Risks")

                    for reason in risk_reasons:
                        st.write(f"• {reason}")

                st.markdown("#### Recommended Next Action")

                if idea_margin <= 0:

                    st.write(
                        "Review pricing and reduce variable "
                        "expenses before purchasing inventory."
                    )

                elif idea_remaining < 0:

                    st.write(
                        "Compare supplier minimum orders, "
                        "negotiate costs, or reduce the "
                        "initial inventory commitment."
                    )

                elif idea_conversion_rate is None:

                    st.write(
                        "Conduct a controlled, low-cost "
                        "demand test before investing."
                    )

                elif idea_paid_orders == 0:

                    st.write(
                        "Revise the offer and conduct another "
                        "demand test before purchasing inventory."
                    )

                elif decision == "PROMISING":

                    st.write(
                        "Verify supplier quotations and "
                        "consider a small controlled pilot."
                    )

                else:

                    st.write(
                        "Continue testing customer demand "
                        "before committing to inventory."
                    )

            st.caption(
                "Academic prototype | Illustrative "
                "rule-based recommendations. "
                "Not financial or investment advice."
            )

    # ------------------------------------------------------
    # RETURN NAVIGATION
    # ------------------------------------------------------

    st.divider()

    if st.button(
        "Return to Home",
        key="return_evaluate",
    ):
        st.session_state["page"] = "home"
        st.rerun()

# ==========================================================
# END | EVALUATE MY IDEA
# ==========================================================
