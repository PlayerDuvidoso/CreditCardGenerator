import flet as ft
import generator

def main(page: ft.Page):
    page.title = 'ToDoing'
    page.window_height = 639
    page.window_width = 816
    page.padding = 0
    
    cc_list = []
    
    def generate(e):
        cc_container.visible=True
        for card in range(1, int(generator_amount.value)+1):
            match generator_brand.value:
                case 'MASTERCARD':
                    cc_list.append(generator.CCNumGen('MASTERCARD').card_list[0])
                case 'VISA':
                    cc_list.append(generator.CCNumGen('VISA').card_list[0])
                case 'AMERICAN EXPRESS':
                    cc_list.append(generator.CCNumGen('AMERICAN EXPRESS').card_list[0])
        current, all = str(cc_count.value).split('/')
        if current != '0':
            updateCard(e, int(current))
            page.update()
            return
        updateCard()
        page.update()
    
    def updateCard(e=None, index=1):
        if index <= 0 or index >= len(cc_list)+1:
            return
        cc_count.visible = True
        cc_count.value = f'{index}/{len(cc_list)}'
        cc_brand.value = cc_list[index-1]['cc_type']
        cc_cvv.value = cc_list[index-1]['cc_cvv']
        cc_number.value = cc_list[index-1]['cc_num']
        cc_exp.value = cc_list[index-1]['cc_exp']
        cc_holder.value = cc_list[index-1]['cc_holder']
        page.update()
    
    def nextCard(e):
        current, all = str(cc_count.value).split('/')
        next_card = int(current)+1
        updateCard(e, next_card)
    
    def previousCard(e):
        current, all = str(cc_count.value).split('/')
        next_card = int(current)-1
        updateCard(e, next_card)
    
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
            ft.ElevatedButton(text='Generate', style=ft.ButtonStyle(bgcolor='#D35400', color='#ECF0F1', overlay_color=ft.colors.ORANGE_900), width=180, height=40, on_click=generate)
        ])),
                                                                                                                                            ft.Container(padding=ft.padding.only(top=30, left=30, right=30), bgcolor='#ECF0F1', width=540, height=600, content=ft.Column(spacing=12, horizontal_alignment='center', controls=[
                                                                                                                                                ft.Text('RESULTS', color='#D35400', size=18, weight=ft.FontWeight.W_500),
                                                                                                                                                ft.Divider(height=0),
                                                                                                                                                ft.Divider(height=143, opacity=0),
                                                                                                                                                ft.Row(spacing=5, visible=False, alignment='center', controls=[
                                                                                                                                                    ft.IconButton(icon=ft.icons.ARROW_LEFT, icon_size=50, scale=1, on_click=previousCard),
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
                                                                                                                                                    ft.IconButton(icon=ft.icons.ARROW_RIGHT, icon_size=50, scale=1, on_click=nextCard)]),
                                                                                                                                                ft.Text(value='0/0', size=12, color='#000000', visible=False)
                                                                                                                                                ]))]))]))
    generator_container = page.controls[0].controls[0].content.controls[0].content
    generator_amount = generator_container.controls[4]
    generator_brand = generator_container.controls[3]
    cc_container = page.controls[0].controls[0].content.controls[1].content.controls[3]
    cc_brand = cc_container.controls[1].content.controls[0]
    cc_number = cc_container.controls[1].content.controls[2].controls[0]
    cc_exp = cc_container.controls[1].content.controls[2].controls[1]
    cc_holder = cc_container.controls[1].content.controls[3].controls[0]
    cc_cvv = cc_container.controls[1].content.controls[3].controls[1]
    cc_count = page.controls[0].controls[0].content.controls[1].content.controls[4]

if __name__ == '__main__':
    ft.app(target=main)