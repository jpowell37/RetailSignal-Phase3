
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

    .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h2, h3 {
        font-weight: 650;
        letter-spacing: -0.3px;
    }

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


# ==========================================================
# RETAILSIGNAL | LUXURY FINTECH HOMEPAGE
# ==========================================================

if st.session_state["page"] == "home":

    st.title("RetailSignal")

    st.write(
        "Discover promising products, evaluate financial feasibility, "
        "and make informed investment decisions before committing capital."
    )

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

    feature_col1, feature_col2, feature_col3 = st.columns(
        3, gap="medium"
    )

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
# RETAILSIGNAL | DISCOVER OPPORTUNITIES
# ==========================================================

if st.session_state.get("page") == "discover":

    st.caption("RETAILSIGNAL / OPPORTUNITY INTELLIGENCE")
    st.title("Discover Opportunities")

    st.write(
        "Compare illustrative e-commerce products using your budget, "
        "estimated contribution margins, and demand-test evidence."
    )

    with st.container(border=True):

        st.subheader("Your Business Profile")
        left, right = st.columns(2)

        with left:
            category = st.selectbox(
                "Product Category",
                [
                    "Beauty & Personal Care",
                    "Fashion & Accessories",
                    "Home & Lifestyle",
                    "Other Consumer Products",
                    "All Categories",
                ],
                key="discover_category_final",
            )

        with right:
            capital = st.number_input(
                "Available Startup Capital ($)",
                min_value=0.0,
                value=2500.0,
                step=100.0,
                format="%.2f",
                key="discover_capital_final",
            )

        goal = st.selectbox(
            "Primary Business Goal",
            [
                "Discover a promising product opportunity",
                "Validate demand before investing",
                "Launch a small e-commerce business",
                "Evaluate an existing product idea",
            ],
            key="discover_goal_final",
        )

        analyze = st.button(
            "Analyze Opportunities",
            type="primary",
            use_container_width=True,
            key="discover_analyze_final",
        )

    if analyze:
        st.session_state["discover_results_visible"] = True

    if st.session_state.get("discover_results_visible", False):

        # Additional hypothetical demonstration products.
        demo_products = [
            dict(
                product="Peptide Lip Balm",
                category="Beauty & Personal Care",
                estimated_unit_cost=3.80,
                minimum_order_quantity=100,
                packaging_cost_per_unit=1.20,
                estimated_selling_price=16.00,
                other_variable_cost_per_sale=5.00,
                test_visitors=150,
                test_paid_orders=18,
            ),
            dict(
                product="Travel Makeup Pouch",
                category="Beauty & Personal Care",
                estimated_unit_cost=4.00,
                minimum_order_quantity=80,
                packaging_cost_per_unit=1.00,
                estimated_selling_price=15.00,
                other_variable_cost_per_sale=5.00,
                test_visitors=120,
                test_paid_orders=4,
            ),
            dict(
                product="Everyday Canvas Tote",
                category="Fashion & Accessories",
                estimated_unit_cost=6.50,
                minimum_order_quantity=100,
                packaging_cost_per_unit=1.00,
                estimated_selling_price=24.00,
                other_variable_cost_per_sale=8.00,
                test_visitors=140,
                test_paid_orders=15,
            ),
            dict(
                product="Ceramic Trinket Tray",
                category="Home & Lifestyle",
                estimated_unit_cost=5.00,
                minimum_order_quantity=75,
                packaging_cost_per_unit=1.50,
                estimated_selling_price=22.00,
                other_variable_cost_per_sale=7.00,
                test_visitors=130,
                test_paid_orders=13,
            ),
            dict(
                product="Reusable Desk Organizer",
                category="Other Consumer Products",
                estimated_unit_cost=8.00,
                minimum_order_quantity=60,
                packaging_cost_per_unit=1.50,
                estimated_selling_price=27.00,
                other_variable_cost_per_sale=9.00,
                test_visitors=110,
                test_paid_orders=5,
            ),
        ]

        def get_field(record, *names):
            for name in names:
                value = record.get(name)
                if value is not None and value != "":
                    return value
            return None

        def normalize_category(value):
            value = str(value or "").lower()

            if "beauty" in value or "personal care" in value:
                return "Beauty & Personal Care"

            if "fashion" in value or "accessor" in value:
                return "Fashion & Accessories"

            if "home" in value or "lifestyle" in value:
                return "Home & Lifestyle"

            return "Other Consumer Products"

        original_products = [dict(item) for item in sample_products]

        product_records = [
            (item, False) for item in original_products
        ]

        product_records += [
            (item, True) for item in demo_products
        ]

        assessments = []

        for product, is_demo in product_records:

            product_category = normalize_category(
                product.get("category")
            )

            if (
                category != "All Categories"
                and product_category != category
            ):
                continue

            name = get_field(
                product, "product", "product_name", "name"
            ) or "Sample Product"

            unit_raw = get_field(
                product,
                "estimated_unit_cost",
                "unit_cost",
                "supplier_cost",
            )

            moq_raw = get_field(
                product,
                "minimum_order_quantity",
                "moq",
                "minimum_order",
            )

            packaging_raw = get_field(
                product,
                "packaging_cost_per_unit",
                "packaging_cost",
            )

            price_raw = get_field(
                product,
                "estimated_selling_price",
                "selling_price",
                "price",
            )

            other_raw = get_field(
                product,
                "other_variable_cost_per_sale",
                "other_variable_cost",
            )

            visitors_raw = get_field(
                product, "test_visitors", "visitors"
            )

            orders_raw = get_field(
                product, "test_paid_orders", "paid_orders"
            )

            test_spend_raw = get_field(
                product, "test_spend", "demand_test_spend"
            )

            unit_cost = (
                float(unit_raw)
                if unit_raw is not None else None
            )

            moq = (
                int(moq_raw)
                if moq_raw is not None else None
            )

            packaging = (
                float(packaging_raw)
                if packaging_raw is not None else 0.0
            )

            price = (
                float(price_raw)
                if price_raw is not None else None
            )

            other_cost = (
                float(other_raw)
                if other_raw is not None else None
            )

            visitors = (
                int(visitors_raw)
                if visitors_raw is not None else None
            )

            orders = (
                int(orders_raw)
                if orders_raw is not None else None
            )

            test_spend = (
                float(test_spend_raw)
                if test_spend_raw is not None else None
            )

            commitment = (
                (unit_cost + packaging) * moq
                if unit_cost is not None
                and moq is not None
                and moq > 0
                else None
            )

            remaining = (
                capital - commitment
                if commitment is not None else None
            )

            margin = (
                price - unit_cost - packaging - other_cost
                if price is not None
                and price > 0
                and unit_cost is not None
                and other_cost is not None
                else None
            )

            demand_valid = (
                visitors is not None
                and visitors > 0
                and orders is not None
                and 0 <= orders <= visitors
            )

            conversion = (
                100 * orders / visitors
                if demand_valid else None
            )

            risks = []

            if remaining is not None and remaining < 0:
                risks.append(
                    "The initial inventory commitment "
                    "exceeds your budget."
                )

            if margin is not None and margin <= 0:
                risks.append(
                    "Estimated variable costs meet or "
                    "exceed the selling price."
                )

            if demand_valid and orders == 0:
                risks.append(
                    "The sample demand test recorded "
                    "zero paid orders."
                )

            if risks:
                status = "NOT READY"

            elif (
                commitment is None
                or margin is None
                or not demand_valid
            ):
                status = "INSUFFICIENT DATA"

            elif visitors >= 100 and orders >= 10:
                status = "PROMISING"

            else:
                status = "POTENTIAL"

            assessments.append(
                dict(
                    name=name,
                    category=product_category,
                    demo=is_demo,
                    unit_cost=unit_cost,
                    moq=moq,
                    packaging=packaging,
                    price=price,
                    other_cost=other_cost,
                    test_spend=test_spend,
                    commitment=commitment,
                    remaining=remaining,
                    margin=margin,
                    visitors=visitors,
                    orders=orders,
                    conversion=conversion,
                    risks=risks,
                    status=status,
                )
            )

        st.divider()
        st.caption("OPPORTUNITY INTELLIGENCE / COMPARISON")
        st.subheader("Your Product Opportunities")

        st.write(
            f"**Category:** {category} | "
            f"**Available capital:** ${capital:,.2f}"
        )

        st.caption(
            f"Your goal: {goal}. Goals guide the analysis; "
            "they do not override the evidence."
        )

        st.info(
            "Additional opportunities and their demand tests "
            "are hypothetical demonstrations. PROMISING is a "
            "preliminary rule-based classification, not a "
            "verified market forecast or guarantee of success."
        )

        if not assessments:

            st.warning(
                "No sample products are available "
                "for this category."
            )

        else:

            order = {
                "PROMISING": 0,
                "POTENTIAL": 1,
                "INSUFFICIENT DATA": 2,
                "NOT READY": 3,
            }

            assessments.sort(
                key=lambda item: (
                    order[item["status"]],
                    -(
                        item["remaining"]
                        if item["remaining"] is not None
                        else -1e9
                    ),
                )
            )

            summary = st.columns(4)

            for col, status in zip(summary, order):
                col.metric(
                    status.title(),
                    sum(
                        item["status"] == status
                        for item in assessments
                    ),
                )

            for item in assessments:

                with st.container(border=True):

                    st.caption(
                        "HYPOTHETICAL DEMONSTRATION — NOT VERIFIED"
                        if item["demo"]
                        else "ORIGINAL SAMPLE RECORD — ILLUSTRATIVE"
                    )

                    st.subheader(item["name"])

                    status = item["status"]

                    if status == "PROMISING":
                        st.success(
                            "PROMISING — Preliminary financial "
                            "and demand thresholds met."
                        )

                    elif status == "POTENTIAL":
                        st.info(
                            "POTENTIAL — Some positive evidence; "
                            "further validation needed."
                        )

                    elif status == "NOT READY":
                        st.error(
                            "NOT READY — Financial or demand "
                            "risks identified."
                        )

                    else:
                        st.warning(
                            "INSUFFICIENT DATA — Missing "
                            "financial or demand evidence."
                        )

                    m1, m2, m3 = st.columns(3)

                    m1.metric(
                        "Initial Commitment",
                        f"${item['commitment']:,.2f}"
                        if item["commitment"] is not None
                        else "Unknown",
                    )

                    m2.metric(
                        "Capital Remaining",
                        f"${item['remaining']:,.2f}"
                        if item["remaining"] is not None
                        else "Unknown",
                    )

                    m3.metric(
                        "Margin per Sale",
                        f"${item['margin']:,.2f}"
                        if item["margin"] is not None
                        else "Unknown",
                    )

                    if item["remaining"] is not None:
                        st.write(
                            "**Budget Fit:** "
                            + (
                                "Affordable"
                                if item["remaining"] >= 0
                                else "Over budget"
                            )
                        )

                    if item["conversion"] is not None:
                        st.write(
                            f"**Demand Test:** "
                            f"{item['orders']} paid orders from "
                            f"{item['visitors']} visitors "
                            f"({item['conversion']:.1f}% conversion)."
                        )

                    else:
                        st.write(
                            "**Demand Test:** Complete visitor/"
                            "order evidence unavailable."
                        )

                    if item["test_spend"] is not None:
                        st.write(
                            f"**Entered Demand-Test Spending:** "
                            f"${item['test_spend']:,.2f} "
                            "(not included in the per-sale margin)."
                        )

                    else:
                        st.caption(
                            "Demand-test spending: not recorded."
                        )

                    st.caption(
                        "Source status: illustrative example. "
                        "Supplier prices and test orders have not "
                        "been independently verified."
                    )

                    for risk in item["risks"]:
                        st.write("• " + risk)

                    if status == "PROMISING":
                        action = (
                            "Verify actual supplier quotes and "
                            "demand, then consider a limited pilot."
                        )

                    elif status == "POTENTIAL":
                        action = (
                            "Conduct additional low-cost demand "
                            "testing before purchasing inventory."
                        )

                    elif status == "INSUFFICIENT DATA":
                        action = (
                            "Collect complete pricing, variable "
                            "costs, and paid-order test data."
                        )

                    elif (
                        item["remaining"] is not None
                        and item["remaining"] < 0
                    ):
                        action = (
                            "Reduce minimum order size or compare "
                            "lower-commitment suppliers."
                        )

                    elif (
                        item["margin"] is not None
                        and item["margin"] <= 0
                    ):
                        action = (
                            "Improve the selling price or "
                            "reduce variable costs."
                        )

                    else:
                        action = (
                            "Revise the offer and test for "
                            "actual customer purchases."
                        )

                    st.write(
                        "**Recommended Next Action:** " + action
                    )

                    # Transfer complete sample records to Evaluate.
                    # Missing values are not fabricated.

                    ready_to_transfer = (
                        item["unit_cost"] is not None
                        and item["moq"] is not None
                        and item["moq"] >= 1
                        and item["price"] is not None
                        and item["price"] > 0
                        and item["other_cost"] is not None
                    )

                    if ready_to_transfer:

                        if st.button(
                            "Select and Evaluate This Product",
                            key=f"transfer_product_{item['name']}",
                            use_container_width=True,
                        ):

                            st.session_state["pending_evaluation"] = {
                                "idea_product_name": item["name"],
                                "idea_capital": float(capital),
                                "idea_selling_price": float(
                                    item["price"]
                                ),
                                "idea_supplier_cost": float(
                                    item["unit_cost"]
                                ),
                                "idea_moq": int(item["moq"]),
                                "idea_packaging_cost": float(
                                    item["packaging"]
                                ),
                                "idea_other_cost": float(
                                    item["other_cost"]
                                ),
                                "idea_visitors": int(
                                    item["visitors"] or 0
                                ),
                                "idea_paid_orders": int(
                                    item["orders"] or 0
                                ),
                                "idea_test_spend": float(
                                    item["test_spend"] or 0
                                ),
                                "idea_source_note": (
                                    "Hypothetical demonstration record"
                                    if item["demo"]
                                    else "Original illustrative sample record"
                                ),
                            }

                            st.session_state["page"] = "evaluate"
                            st.rerun()

                    else:
                        st.caption(
                            "Transfer unavailable: this sample lacks "
                            "complete pricing or supplier-cost inputs. "
                            "Use Evaluate My Idea to enter your own."
                        )

    st.divider()

    if st.button(
        "Return to Home",
        key="discover_return_final",
    ):
        st.session_state["page"] = "home"
        st.rerun()


# ==========================================================
# RETAILSIGNAL | EVALUATE MY IDEA
# ==========================================================

if st.session_state.get("page") == "evaluate":

    # Apply transferred data before creating keyed widgets.

    incoming = st.session_state.pop(
        "pending_evaluation", None
    )

    if incoming is not None:

        st.session_state["idea_source_note"] = incoming.pop(
            "idea_source_note", "Illustrative record"
        )

        for field_key, field_value in incoming.items():
            st.session_state[field_key] = field_value

        st.session_state["supplier_a_evidence"] = (
            "Hypothetical estimate"
        )

        st.session_state["supplier_b_evidence"] = (
            "Hypothetical estimate"
        )

    st.caption("RETAILSIGNAL / FINANCIAL INTELLIGENCE")
    st.title("Evaluate My Idea")

    st.write(
        "Turn your product idea into an evidence-based business "
        "decision. Compare sourcing commitments, analyze unit "
        "economics, and assess customer demand before investing."
    )

    if st.session_state.get("idea_source_note"):
        st.info(
            "Loaded from Discover: "
            + st.session_state["idea_source_note"]
            + ". All values are editable and unverified; "
            "confirm costs and demand evidence before relying on them."
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

            supplier_a_evidence = st.selectbox(
                "Supplier A Price Evidence",
                [
                    "Hypothetical estimate",
                    "Indicative catalog price (user-reported)",
                    "Supplier quote (user-reported; not verified)",
                ],
                key="supplier_a_evidence",
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

            supplier_b_evidence = st.selectbox(
                "Supplier B Price Evidence",
                [
                    "Hypothetical estimate",
                    "Indicative catalog price (user-reported)",
                    "Supplier quote (user-reported; not verified)",
                ],
                key="supplier_b_evidence",
            )

    st.caption(
        "Price evidence is user-selected and not independently "
        "authenticated by RetailSignal. Supplier B is an editable "
        "comparison scenario, not a quote linked to the selected product."
    )

    # ------------------------------------------------------
    # 03 | OPERATING COSTS
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

        idea_test_spend = st.number_input(
            "Demand-Test Spending ($)",
            min_value=0.0,
            value=0.0,
            step=10.0,
            format="%.2f",
            key="idea_test_spend",
        )

        st.caption(
            "Record the amount already spent on this test. "
            "This is separate from per-sale variable expenses and "
            "is not subtracted again from current available capital. "
            "Demand results are user-entered, not independently verified."
        )

    st.divider()

    run_analysis = st.button(
        "Generate Financial Intelligence Report",
        type="primary",
        use_container_width=True,
        key="run_idea_analysis",
    )

    # ======================================================
    # FINANCIAL INTELLIGENCE REPORT
    # ======================================================

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
                "RETAILSIGNAL / OPPORTUNITY ANALYSIS REPORT"
            )

            st.title("Financial Intelligence Report")
            st.write(f"**Product:** {product_name}")

            st.caption(
                "Preliminary assessment based on entered "
                "financial assumptions and demand evidence."
            )

            # ----------------------------------------------
            # FINANCIAL OVERVIEW
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
                f"Supplier A: {supplier_a_evidence}. "
                f"Supplier B: {supplier_b_evidence}. "
                "These statuses are user-reported and not verified "
                "by RetailSignal."
            )

            # ----------------------------------------------
            # PROFITABILITY ANALYSIS
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
            # DEMAND-TEST EXPENSE REVIEW
            # ----------------------------------------------

            st.markdown("#### Demand-Test Expense Review")

            test_col1, test_col2 = st.columns(2)

            test_col1.metric(
                "Recorded Test Spending",
                f"${idea_test_spend:,.2f}"
            )

            if idea_paid_orders > 0:

                test_col2.metric(
                    "Test Spend per Paid Order",
                    f"${idea_test_spend / idea_paid_orders:,.2f}",
                )

            else:

                test_col2.metric(
                    "Test Spend per Paid Order",
                    "N/A"
                )

            st.caption(
                "Test spending is historical expenditure entered "
                "by the user. It is not included in the per-sale "
                "contribution margin or subtracted from the current "
                "startup-capital figure. A zero-order test cannot "
                "yield a cost per order."
            )

            # ----------------------------------------------
            # INVESTMENT READINESS
            # ----------------------------------------------

            st.divider()

            st.caption(
                "RETAILSIGNAL / EXECUTIVE DECISION SUMMARY"
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

                st.write(
                    f"**Test Expense:** ${idea_test_spend:,.2f} "
                    "recorded separately from estimated unit economics."
                )

                st.write(
                    "**Source Quality:** Supplier A — "
                    + supplier_a_evidence
                    + "; Supplier B — "
                    + supplier_b_evidence
                    + ". Both statuses are user-reported, not "
                    "independently authenticated."
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
                "rule-based recommendations. A PROMISING result "
                "does not establish verified investment readiness. "
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
