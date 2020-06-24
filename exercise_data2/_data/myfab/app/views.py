import calendar

from flask_appbuilder import ModelView
from flask_appbuilder.charts.views import GroupByChartView
from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.models.sqla.interface import SQLAInterface

from . import appbuilder, db
from .models import Contact, ContactGroup, Gender, Test, Try, Socials


def fill_gender():
    try:
        db.session.add(Gender(name="Male"))
        db.session.add(Gender(name="Female"))
        db.session.commit()
    except Exception:
        db.session.rollback()


class ContactModelView(ModelView):
    datamodel = SQLAInterface(Contact)

    list_columns = ["name", "personal_celphone", "birthday", "contact_group.name"]

    base_order = ("name", "asc")
    show_fieldsets = [
        ("Summary", {"fields": ["name", "gender", "contact_group"]}),
        (
            "Personal Info",
            {
                "fields": [
                    "address",
                    "birthday",
                    "personal_phone",
                    "personal_celphone",
                ],
                "expanded": False,
            },
        ),
    ]

    add_fieldsets = [
        ("Summary", {"fields": ["name", "gender", "contact_group"]}),
        (
            "Personal Info",
            {
                "fields": [
                    "address",
                    "birthday",
                    "personal_phone",
                    "personal_celphone",
                ],
                "expanded": False,
            },
        ),
    ]

    edit_fieldsets = [
        ("Summary", {"fields": ["name", "gender", "contact_group"]}),
        (
            "Personal Info",
            {
                "fields": [
                    "address",
                    "birthday",
                    "personal_phone",
                    "personal_celphone",
                ],
                "expanded": False,
            },
        ),
    ]


class GroupModelView(ModelView):
    datamodel = SQLAInterface(ContactGroup)
    related_views = [ContactModelView]


def pretty_month_year(value):
    return calendar.month_name[value.month] + " " + str(value.year)


def pretty_year(value):
    return str(value.year)


class ContactTimeChartView(GroupByChartView):
    datamodel = SQLAInterface(Contact)

    chart_title = "Grouped Birth contacts"
    chart_type = "AreaChart"
    label_columns = ContactModelView.label_columns
    definitions = [
        {
            "group": "month_year",
            "formatter": pretty_month_year,
            "series": [(aggregate_count, "group")],
        },
        {
            "group": "year",
            "formatter": pretty_year,
            "series": [(aggregate_count, "group")],
        },
    ]



class TestView2(ModelView):
    datamodel = SQLAInterface(Try)

    list_columns = ["name", "socials"]

    show_fieldsets = [
            ("Info", {"fields": ["name", "socials"]}),
    ]

    add_fieldsets = [
            ("Info", {"fields": ["name", "socials"]}),
    ]

    edit_fieldsets = [
            ("Info", {"fields": ["name", "socials"]}),
    ]


class SocialsView(ModelView):
    datamodel = SQLAInterface(Socials)
    related_views = [TestView2]


class TestView(ModelView):
    datamodel = SQLAInterface(Test)

    list_columns = ["name", "socials"]

    base_order = ("name", "asc")

    show_fieldsets = [
        ("Test?", {"fields": ["name", "socials"]}),
        (
            "Socials",
            {
                "fields": [
                    "twitter",
                    "instagram",
                    "facebook",
                ],
                "expanded": False,
            },
        ),
    ]

    add_fieldsets = [
        ("Test", {"fields": ["name", "socials"]}),
        (
            "Socials",
            {
                "fields": [
                    "twitter",
                    "instagram",
                    "facebook",
                ],
                "expanded": False,
            },
        ),
    ]

    edit_fieldsets = [
        ("Test", {"fields": ["name", "socials"]}),
        (
            "Socials",
            {
                "fields": [
                    "twitter",
                    "instagram",
                    "facebook",
                ],
                "expanded": False,
            },
        ),
    ]
    


db.create_all()
fill_gender()
appbuilder.add_view(
    GroupModelView,
    "List Groups",
    icon="fa-folder-open-o",
    category="Contacts",
    category_icon="fa-envelope",
)
appbuilder.add_view(
    ContactModelView, "List Contacts", icon="fa-envelope", category="Contacts"
)
appbuilder.add_separator("Contacts")
appbuilder.add_view(
    ContactTimeChartView,
    "Contacts Birth Chart",
    icon="fa-dashboard",
    category="Contacts",
)
appbuilder.add_view(
    TestView,
    "Testing",
    icon="fa-folder-open-o",
    category="Test",
    category_icon="fa-dashboard",
)
appbuilder.add_separator("Test")
appbuilder.add_view(
    TestView2,
    "Another",
    icon="fa-envelope",
    category="Test",
)

appbuilder.add_view(
    SocialsView,
    "Socials",
    icon="fa-folder-open-o",
    category="Test",
)
