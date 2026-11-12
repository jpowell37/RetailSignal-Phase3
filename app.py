
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



    

    

    





    

           


         



if st.session_state.get("page") == "discover":
    st.divider()
    st.header("Entrepreneur Discovery Assessment")

    st.write(
        "Let's explore potential product opportunities based on "
        "your interests, available capital, and business goals."
    )

    st.subheader("Your Product Interests")

    interest = st.selectbox(
        "Which product category interests you most?",
        [
            "Select a category",
            "Beauty & Personal Care",
            "Fashion & Accessories",
            "Home & Lifestyle",
            "Other Consumer Products"
        ]
    )

    st.subheader("Available Startup Capital")

    capital = st.number_input(
        "How much money do you have available to invest?",
        min_value=0.0,
        value=1500.0,
        step=100.0,
        format="%.2f"
    )

    st.subheader("Your Business Goals")

    goal = st.selectbox(
        "What is your primary business goal?",
        [
            "Select a goal",
            "Discover a promising product opportunity",
            "Validate demand before investing",
            "Launch a small e-commerce business",
            "Evaluate an existing product idea"
        ]
    )

    if st.button("Analyze Opportunities", type="primary"):
        if interest == "Select a category" or goal == "Select a goal":
            st.warning("Please select a product category and business goal.")
        else:
            
            matching_products = [
                product for product in sample_products
                if product["category"] == interest
            ]

            st.subheader("Potential Product Opportunities")

            
            if matching_products:
                for product in matching_products:
                    st.write(product["product"])

                    
                    selling_price = product.get("estimated_selling_price")

                    if selling_price is None:
                        st.warning(
                            "INSUFFICIENT DATA — A proposed selling price "
                            "is required before profitability can be evaluated."
                        )

                    if selling_price is not None:
                        st.write(
                            f"Proposed selling price: ${selling_price:,.2f}"
                        )
                    
                    if selling_price is not None:
                        other_variable_cost = product.get(
                            "other_variable_cost_per_sale", 0
                        )

                        

                        total_variable_cost = (
                            product["estimated_unit_cost"]
                            + product.get("packaging_cost_per_unit", 0)
                            + other_variable_cost
                        )

                        contribution_margin = selling_price - total_variable_cost

                        if selling_price > 0:
                            contribution_margin_ratio = (
                                contribution_margin / selling_price
                            ) * 100

                            st.write(
                                f"Estimated contribution margin ratio: {contribution_margin_ratio:.1f}%"
                            )
                        else:
                            st.warning(
                                "A selling price above $0 is required "
                                "to calculate the contribution margin ratio."
                            )

                        st.write(
                            f"Estimated variable expenses per sale: ${total_variable_cost:,.2f}"
                        )

                        st.write(
                            f"Estimated contribution margin per sale: ${contribution_margin:,.2f}"
                        )

                        if contribution_margin <= 0:
                            st.error(
                                "Financial Risk: Estimated variable expenses "
                                "equal or exceed the selling price. Review "
                                "pricing and costs before proceeding."
                            )
                        else:
                            st.info(
                                "Estimated sales revenue exceeds variable "
                                "expenses. However, a positive contribution "
                                "margin does not establish profitability. "
                                "Fixed costs and consumer demand still "
                                "require evaluation."
                            )

                    inventory_cost = (
                        product["estimated_unit_cost"]
                        * product["minimum_order_quantity"]
                    )

                    
                    packaging_cost = (
                        product.get("packaging_cost_per_unit", 0)
                        * product["minimum_order_quantity"]
                    )

                    total_initial_commitment = inventory_cost + packaging_cost

                    remaining_capital = capital - total_initial_commitment

                    test_visitors = product.get("test_visitors")
                    test_spend = product.get("test_spend")
                    test_paid_orders = product.get("test_paid_orders")

                    if test_visitors is None or test_paid_orders is None:
                        st.warning(
                            "INSUFFICIENT DATA — Demand-test results are "
                            "not available. Purchasing demand cannot yet "
                            "be evaluated."
                        )

                    total_initial_commitment = inventory_cost + packaging_cost
                    if (
                        test_visitors is not None
                        and test_paid_orders is not None
                        and test_visitors > 0
                    ):
                        conversion_rate = (
                            test_paid_orders / test_visitors
                        ) * 100

                        st.subheader("Demand Validation Results")
                        st.write(
                            f"Test visitors: {test_visitors}"
                        )
                        st.write(
                            f"Reported paid orders: {test_paid_orders}"
                        )
                        st.write(
                            f"Observed conversion rate: {conversion_rate:.1f}%"
                        )

                        if test_paid_orders == 0:
                            st.warning(
                                "Demand Risk: No paid orders were reported "
                                "during this limited test. Consider revising "
                                "the offer or testing again before purchasing inventory."
                            )
                        else:
                            st.info(
                                "Paid orders were reported during the test. "
                                "Additional validation is still needed before "
                                "making an inventory investment."
                            )

                        st.subheader("Preliminary Recommendation")

                        
                        risk_reasons = []

                        if remaining_capital < 0:
                            risk_reasons.append(
                                "The initial inventory and packaging commitment "
                                "exceeds available startup capital."
                            )

                        if contribution_margin <= 0:
                            risk_reasons.append(
                                "Estimated variable expenses equal or exceed "
                                "the proposed selling price."
                            )

                        if test_paid_orders == 0:
                            risk_reasons.append(
                                "The demand test reported no paid orders."
                            )

                        if (
                            test_paid_orders == 0
                            or remaining_capital < 0
                            or contribution_margin <= 0
                        ):

                            
                            st.error(
                                "NOT READY — One or more financial or demand "
                                "risks require attention. Review available "
                                "capital, contribution margin, and paid-order "
                                "evidence before committing to inventory."
                            )

                            st.write("**Identified Risk Factors:**")

                            for reason in risk_reasons:
                                st.write(f"• {reason}")

                        
                        elif test_visitors >= 100 and test_paid_orders >= 10:
                            st.success(
                                "PROMISING — Preliminary financial screening "
                                "and illustrative demand criteria are met. "
                                "Consider a small controlled pilot after "
                                "verifying supplier costs and demand evidence."
                            )
                        else:

                            
                            st.info(
                                "POTENTIAL — Initial financial screening "
                                "has passed, and the test reported paid orders. "
                                "However, additional evidence is needed before "
                                "making an inventory investment."
                            )


                        if test_spend is not None:
                            st.write(
                                f"Demand test spending: ${test_spend:,.2f}"
                            )

                    st.write(
                        f"Estimated initial inventory cost: ${inventory_cost:,.2f}"
                    )

                    st.write(
                        f"Estimated packaging cost: ${packaging_cost:,.2f}"
                    )

                    st.write(
                        f"Total initial inventory and packaging commitment: ${total_initial_commitment:,.2f}"
                    )

                    
                    remaining_capital = capital - total_initial_commitment


                    if capital > 0:
                       
                        budget_utilization = (total_initial_commitment / capital) * 100

                        st.write(
                            
f"Inventory and Packaging Budget Utilization: {budget_utilization:.1f}%"

                        )
                        
                        st.progress(min(total_initial_commitment / capital, 1.0))

                    else:
                        st.warning(
                            "Budget utilization cannot be calculated "
                            "because available startup capital is $0."
                        )

                    st.write(
                        f"Available startup capital: ${capital:,.2f}"
                    )

                    st.write(
                        
f"Remaining capital after inventory and packaging: ${remaining_capital:,.2f}"

                    )

                    
                    if remaining_capital < 0:
                        st.error(
                            "The estimated inventory and packaging commitment "
                            "exceeds your available startup capital. Consider "
                            "reducing costs, negotiating a lower minimum order "
                            "quantity, or evaluating another opportunity."
                        )
                    else:
                        st.info(
                            "The estimated inventory and packaging commitment "
                            "fits within your available capital. However, "
                            "shipping, marketing, selling expenses, and "
                            "consumer demand still require evaluation."
                        )


            else:
                st.info("No sample products are available for this category.")


    if st.button("Return to Home"):
        st.session_state["page"] = "home"
        st.rerun()
  
        st.rerun()






if st.session_state.get("page") == "evaluate":
        st.divider()
        st.header("Evaluate My Idea")

        st.write(
            "Research your product idea, compare suppliers, "
            "and evaluate financial feasibility before investing."
        )

        product_name = st.text_input(
            "What product would you like to evaluate?",
            placeholder="Example: Hydrating Lip Oil"
        )

        idea_capital = st.number_input(
            "How much startup capital do you have available?",
            min_value=0.0,
            value=1500.0,
            step=100.0,
            format="%.2f",
            key="idea_capital"
        )

        idea_selling_price = st.number_input(
            "What is your proposed selling price per unit?",
            min_value=0.0,
            value=18.0,
            step=1.0,
            format="%.2f",
            key="idea_selling_price"
        )

        idea_supplier_cost = st.number_input(
            "What is your estimated supplier cost per unit?",
            min_value=0.0,
            value=4.50,
            step=0.50,
            format="%.2f",
            key="idea_supplier_cost"
        )

        supplier_b_cost = st.number_input(
            "Supplier B: Estimated cost per unit ($)",
            min_value=0.0,
            value=5.00,
            step=0.50,
            format="%.2f",
            key="supplier_b_cost"
        )

        idea_packaging_cost = st.number_input(
            "What is your estimated packaging cost per unit?",
            min_value=0.0,
            value=1.75,
            step=0.25,
            format="%.2f",
            key="idea_packaging_cost"
        )

        supplier_b_moq = st.number_input(
            "Supplier B: Minimum order quantity",
            min_value=1,
            value=100,
            step=1,
            key="supplier_b_moq"
        )

        idea_moq = st.number_input(
            "What is the supplier's minimum order quantity?",
            min_value=1,
            value=150,
            step=1,
            key="idea_moq"
        )

        idea_other_cost = st.number_input(
            "What are your other estimated variable expenses per sale?",
            min_value=0.0,
            value=9.24,
            step=0.25,
            format="%.2f",
            key="idea_other_cost"
        )

        idea_visitors = st.number_input(
            "How many visitors participated in your demand test?",
            min_value=0,
            value=0,
            step=1,
            key="idea_visitors"
        )

        
        idea_paid_orders = st.number_input(
            "How many paid orders did your demand test generate?",
            min_value=0,
            value=0,
            step=1,
            key="idea_paid_orders"
        )


        if st.button("Evaluate Financial Feasibility"):
            idea_initial_cost = (
                idea_supplier_cost + idea_packaging_cost
            ) * idea_moq

            supplier_b_initial_cost = (
                supplier_b_cost + idea_packaging_cost
            ) * supplier_b_moq

            st.subheader("Supplier Comparison")

            supplier_col1, supplier_col2 = st.columns(2)

            with supplier_col1:
                st.metric(
                    "Supplier A: Initial Commitment",
                    f"${idea_initial_cost:,.2f}"
                )

                st.caption(f"Unit cost: ${idea_supplier_cost:,.2f}")
                st.caption(f"Minimum order: {idea_moq} units")

            with supplier_col2:
                st.metric(
                    "Supplier B: Initial Commitment",
                    f"${supplier_b_initial_cost:,.2f}"
                )

                st.caption(f"Unit cost: ${supplier_b_cost:,.2f}")
                st.caption(f"Minimum order: {supplier_b_moq} units")

            if supplier_b_initial_cost < idea_initial_cost:
                st.info(
                    "Supplier B requires less upfront capital, "
                    "although its unit price may be higher. "
                    "Compare minimum order quantities and total "
                    "costs before selecting a supplier."
                )
            elif supplier_b_initial_cost > idea_initial_cost:
                st.info(
                    "Supplier A requires less upfront capital. "
                    "Review unit prices and minimum order quantities "
                    "before selecting a supplier."
                )
            else:
                st.info(
                    "Both suppliers require the same estimated "
                    "initial inventory and packaging commitment."
                )

            idea_remaining = idea_capital - idea_initial_cost

            idea_variable_cost = (
                idea_supplier_cost
                + idea_packaging_cost
                + idea_other_cost
            )

            idea_margin = idea_selling_price - idea_variable_cost

            if idea_visitors > 0:
                idea_conversion_rate = (
                    idea_paid_orders / idea_visitors
                ) * 100
            else:
                idea_conversion_rate = None

            st.subheader("Financial Feasibility Results")
            
            
            
            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    label="Estimated Initial Commitment",
                    value=f"${idea_initial_cost:,.2f}"
                )

            with col2:
                st.metric(
                    label="Remaining Startup Capital",
                    value=f"${idea_remaining:,.2f}"
                )
           
            st.write("**Capital Utilization**")

            if idea_capital > 0:
                utilization = (idea_initial_cost / idea_capital) * 100
                st.progress(min(utilization / 100, 1.0))
                st.caption(
                    f"{utilization:.1f}% of available startup capital committed."
                )
            else:
                st.warning(
                    "Capital utilization cannot be calculated with $0 available."
                )



            st.write(
                f"Estimated variable cost per sale: ${idea_variable_cost:,.2f}"
            )

            
            st.metric(
                label="Estimated Contribution Margin Per Sale",
                value=f"${idea_margin:,.2f}"
            )


            st.subheader("Demand Validation Results")

            if idea_conversion_rate is not None:
                st.write(
                    f"Test visitors: {idea_visitors}"
                )
                st.write(
                    f"Reported paid orders: {idea_paid_orders}"
                )
                st.write(
                    f"Observed conversion rate: {idea_conversion_rate:.1f}%"
                )
            else:
                st.warning(
                    "INSUFFICIENT DATA — No demand-test visitors "
                    "have been entered."
                )

            
            st.divider()
            st.caption("RETAILSIGNAL | OPPORTUNITY DECISION SUMMARY")
            st.subheader("Investment Readiness Assessment")

            if idea_margin <= 0:
                st.error(
                    "NOT READY — Estimated variable expenses equal "
                    "or exceed the proposed selling price."
                )

            elif idea_remaining < 0:
                st.error(
                    "NOT READY — Initial inventory and packaging costs "
                    "exceed available startup capital."
                )

            elif idea_conversion_rate is None:
                st.warning(
                    "INSUFFICIENT DATA — Complete a demand test "
                    "before making an inventory decision."
                )

            elif idea_paid_orders == 0:
                st.error(
                    "NOT READY — No paid orders were reported. "
                    "Further demand validation is recommended."
                )

            elif idea_visitors >= 100 and idea_paid_orders >= 10:
                st.success(
                    "PROMISING — Preliminary financial and illustrative "
                    "demand criteria are met. Consider a controlled pilot "
                    "after verifying supplier costs and demand evidence."
                )

            else:
                st.info(
                    "POTENTIAL — Some positive demand evidence exists, "
                    "but further validation is recommended."
                )

            st.caption(
                "Preliminary assessment using illustrative criteria. "
                "Results do not guarantee profitability or future sales."
            )



            st.markdown("#### Decision Rationale")

            st.write(
                f"**Financial Evidence:** Estimated contribution margin "
                f"is ${idea_margin:,.2f} per sale, with "
                f"${idea_remaining:,.2f} remaining startup capital."
            )

            if idea_conversion_rate is not None:
                st.write(
                    f"**Demand Evidence:** {idea_paid_orders} paid orders "
                    f"from {idea_visitors} visitors, representing "
                    f"a {idea_conversion_rate:.1f}% observed conversion rate."
                )
            else:
                st.write(
                    "**Demand Evidence:** Insufficient information "
                    "to evaluate purchasing demand."
                )

            st.markdown("#### Recommended Next Action")

            if idea_margin <= 0:
                st.write(
                    "Review your pricing and reduce variable expenses "
                    "before investing in inventory."
                )
            elif idea_remaining < 0:
                st.write(
                    "Compare suppliers, negotiate a lower minimum order "
                    "quantity, or reduce upfront costs."
                )
            elif idea_conversion_rate is None:
                st.write(
                    "Conduct a small, low-cost demand test to gather "
                    "evidence of customer purchasing interest."
                )
            elif idea_paid_orders == 0:
                st.write(
                    "Revise your product offer or marketing approach "
                    "and run another controlled demand test before "
                    "purchasing inventory."
                )
            elif idea_visitors >= 100 and idea_paid_orders >= 10:
                st.write(
                    "Consider a small controlled pilot after verifying "
                    "supplier quotations, fulfillment costs, and demand evidence."
                )
            else:
                st.write(
                    "Continue validating customer demand and reviewing "
                    "cost assumptions before committing to inventory."
                )


         

        if st.button("Return to Home", key="return_evaluate"):
            st.session_state["page"] = "home"
            st.rerun()

       
