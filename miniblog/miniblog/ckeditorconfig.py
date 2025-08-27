# CKEDITOR_5_CONFIGS = {
#     'default': {
#         'toolbar': [
#             'heading', '|',
#             'bold', 'italic', 'link', 'underline', 'strikethrough', '|',
#             'bulletedList', 'numberedList', 'blockQuote', '|',
#             'undo', 'redo', 
#         ],
#         'height': 300,
#         'width': '100%',
#     }
# }


customColorPalette = [
    { 'color': 'hsl(4, 90%, 58%)', 'label': 'Red' },
    { 'color': 'hsl(340, 82%, 52%)', 'label': 'Pink' },
    { 'color': 'hsl(291, 64%, 42%)', 'label': 'Purple' },
    { 'color': 'hsl(262, 52%, 47%)', 'label': 'Deep Purple' },
    { 'color': 'hsl(231, 48%, 48%)', 'label': 'Indigo' },
    { 'color': 'hsl(207, 90%, 54%)', 'label': 'Blue' },
]

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': {
            'items': [
                'heading', '|',
                'bold', 'italic', 'underline', 'strikethrough', 'link',
                'fontColor', 'fontBackgroundColor',   # ✅ add these
                'bulletedList', 'numberedList', 'blockQuote', 'imageUpload',
            ],
        },
        'fontColor': {
            'colors': customColorPalette,   # ✅ apply palette
            'columns': 6,
        },
        'fontBackgroundColor': {
            'colors': customColorPalette,   # ✅ apply palette
            'columns': 6,
        },
    },
    'extends': {
        'toolbar': {
            'items': [
                'heading', '|', 'outdent', 'indent', '|',
                'bold', 'italic', 'link', 'underline', 'strikethrough',
                'fontColor', 'fontBackgroundColor',  # ✅ include here too
                'code','subscript', 'superscript', 'highlight', '|',
                'codeBlock', 'sourceEditing', 'insertImage',
                'bulletedList', 'numberedList', 'todoList', '|',
                'blockQuote', 'imageUpload', '|',
                'fontSize', 'fontFamily', 'mediaEmbed', 'removeFormat',
                'insertTable',
            ],
            'shouldNotGroupWhenFull': True,
        },
        'fontColor': {
            'colors': customColorPalette,
            'columns': 6,
        },
        'fontBackgroundColor': {
            'colors': customColorPalette,
            'columns': 6,
        },
        'table': {
            'contentToolbar': ['tableColumn', 'tableRow', 'mergeTableCells',
                            'tableProperties', 'tableCellProperties'],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette,
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette,
            },
        },
    },
}





# customColorPalette = [
#         {
#             'color': 'hsl(4, 90%, 58%)',
#             'label': 'Red'
#         },
#         {
#             'color': 'hsl(340, 82%, 52%)',
#             'label': 'Pink'
#         },
#         {
#             'color': 'hsl(291, 64%, 42%)',
#             'label': 'Purple'
#         },
#         {
#             'color': 'hsl(262, 52%, 47%)',
#             'label': 'Deep Purple'
#         },
#         {
#             'color': 'hsl(231, 48%, 48%)',
#             'label': 'Indigo'
#         },
#         {
#             'color': 'hsl(207, 90%, 54%)',
#             'label': 'Blue'
#         },
#     ]

# # CKEDITOR_5_CUSTOM_CSS = 'path_to.css' # optional
# # CKEDITOR_5_FILE_STORAGE = "path_to_storage.CustomStorage" # optional
# CKEDITOR_5_CONFIGS = {
# 'default': {
#     'toolbar': {
#         'items': ['customColorPalette','heading', '|', 'bold', 'italic', 'link',
#                     'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],
#                 }

# },
# 'extends': {
#     'blockToolbar': [
#         'paragraph', 'heading1', 'heading2', 'heading3',
#         '|',
#         'bulletedList', 'numberedList',
#         '|',
#         'blockQuote',
#     ],
#     'toolbar': {
#         'items': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
#                     'code','subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
#                 'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
#                 'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
#                 'insertTable',
#                 ],
#         'shouldNotGroupWhenFull': 'true'
#     },
#     'image': {
#         'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
#                     'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
#         'styles': [
#             'full',
#             'side',
#             'alignLeft',
#             'alignRight',
#             'alignCenter',
#         ]

#     },
#     'table': {
#         'contentToolbar': [ 'tableColumn', 'tableRow', 'mergeTableCells',
#         'tableProperties', 'tableCellProperties' ],
#         'tableProperties': {
#             'borderColors': customColorPalette,
#             'backgroundColors': customColorPalette
#         },
#         'tableCellProperties': {
#             'borderColors': customColorPalette,
#             'backgroundColors': customColorPalette
#         }
#     },
#     'heading' : {
#         'options': [
#             { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
#             { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
#             { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
#             { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' }
#         ]
#     }
# },
# 'list': {
#     'properties': {
#         'styles': 'true',
#         'startIndex': 'true',
#         'reversed': 'true',
#     }
# }
# }