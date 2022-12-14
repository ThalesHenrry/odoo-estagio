{
    'name': 'School',
    'version': '15.0.0.0',
    'sumary': 'School Management System',
    'sequence': 1,
    'description': "This is school management system software supported in "
                   "Odoo v15",
    'website': 'https://www.google.com/',
    'category': 'School',
    'author': 'Thales Gregorio',
    'images': [],
    'depends': ['base', 'school'],
    'data': [
        "security/ir.model.access.csv",
        "views/views.xml",
        "wizard/student_fees_update_wizard_view.xml",
        "views/hobby_view.xml",
        "data/hobby.csv",
        "data/school.csv",
        "data/school.student.csv",
        "data/student_data.xml"
    ],
    'application': True
}
