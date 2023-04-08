import flet as ft

def main(page: ft.Page):
    page.title = 'ToDoing'
    page.window_height = 639
    page.window_width = 816
    page.padding = 0
    
    page.add(ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[ft.Container(margin=0, bgcolor='#ECF0F1', width=800, height=600, content=ft.Row(spacing=0, controls=[ft.Container(
        width=260, height=600, padding=ft.padding.only(top=30, left=30, right=30), bgcolor='#ECF0F1', border=ft.border.all(2, '#7F8C8D'), border_radius=ft.border_radius.only(topRight=30, bottomRight=30), content=ft.Column(spacing=10, alignment='start', horizontal_alignment='center', controls=[
            ft.Text("DEN'S GENERATOR", color='#D35400', size=18, weight=ft.FontWeight.W_500),
            ft.Divider(opacity=100, height=0),
            ft.Divider(opacity=0, height=150),
            ft.Dropdown(value='VISA', focused_border_color='#D35400', filled=True, content_padding=ft.padding.only(left=10, right=10), border_radius=20, border_color='#e67e22', bgcolor='#D9D9D9', width=180, height=40, text_style=ft.TextStyle(color='#D35400', size=12), options=[
                                 ft.dropdown.Option("VISA"),
                                 ft.dropdown.Option("MASTERCARD"),
                                 ft.dropdown.Option("AMERICAN EXPRESS")]),
            ft.TextField(value='5', prefix_text='Amount: ', focused_border_color='#D35400', filled=True, bgcolor='#D9D9D9', prefix_style=ft.TextStyle(color='#D35400', size=12), width=180, height=40, border_radius=20, border_color='#e67e22', content_padding=ft.padding.only(left=10, right=10), text_style=ft.TextStyle(color='#D35400', size=12)),
            ft.Divider(height=10, opacity=0),
            ft.ElevatedButton(text='Generate', style=ft.ButtonStyle(bgcolor='#D35400', color='#ECF0F1', overlay_color=ft.colors.ORANGE_900), width=180, height=40)
        ])),
                                                                                                                                            ft.Container(padding=ft.padding.only(top=30, left=30, right=30), bgcolor='#ECF0F1', width=540, height=600, content=ft.Column(spacing=12, horizontal_alignment='center', controls=[
                                                                                                                                                ft.Text('RESULTS', color='#D35400', size=18, weight=ft.FontWeight.W_500),
                                                                                                                                                ft.Divider(height=0),
                                                                                                                                                ft.Divider(height=143, opacity=0),
                                                                                                                                                ft.Row(spacing=5, alignment='center', controls=[
                                                                                                                                                    ft.IconButton(icon=ft.icons.ARROW_LEFT, icon_size=50, scale=1),
                                                                                                                                                    ft.Container(padding=ft.padding.all(15), width=225, height=165, border_radius=20, gradient=ft.LinearGradient(colors=['#2C3E50', '#34495E'], rotation=-90), content=ft.Column(controls=[
                                                                                                                                                        ft.Text(value='VISA', weight=ft.FontWeight.BOLD, size=16),
                                                                                                                                                        ft.Divider(opacity=0, height=50),
                                                                                                                                                        ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                                                                                                                                                            ft.Text('4539398883228199', size=12, selectable=True),
                                                                                                                                                            ft.Text('07/28', size=12, selectable=True)
                                                                                                                                                        ]),
                                                                                                                                                        ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                                                                                                                                                            ft.Text('Benedict Hudson', size=12, selectable=True),
                                                                                                                                                            ft.Text('728', size=12, selectable=True)
                                                                                                                                                        ])
                                                                                                                                                    ])),
                                                                                                                                                    ft.IconButton(icon=ft.icons.ARROW_RIGHT, icon_size=50, scale=1)
                                                                                                                                                    ])
                                                                                                                                            ]))])
    )]))

if __name__ == '__main__':
    ft.app(target=main)