from nicegui import ui

def create():
    @ui.page('/')
    def counter_page():
        # Initialize counter value
        counter = {'value': 0}
        
        # Add pink background to the page
        with ui.column().classes('w-full h-screen bg-pink-50 items-center justify-center p-8'):
            # Create UI elements with pink theme
            ui.label('Simple Counter').classes('text-2xl font-bold mb-8 text-pink-800')
            
            with ui.row().classes('items-center gap-6 bg-white p-6 rounded-lg shadow-lg'):
                decrement_btn = ui.button('-', on_click=lambda: decrement_counter(), color='pink').classes('text-xl w-12 h-12')
                decrement_btn.mark('decrement-btn')
                
                counter_label = ui.label(str(counter['value'])).classes('text-4xl font-mono min-w-20 text-center text-pink-700 font-bold')
                counter_label.mark('counter-display')
                
                increment_btn = ui.button('+', on_click=lambda: increment_counter(), color='pink').classes('text-xl w-12 h-12')
                increment_btn.mark('increment-btn')
            
            # Add a decorative pink accent
            ui.label('Click the buttons to count!').classes('text-pink-600 mt-4 text-sm')
        
        def increment_counter():
            counter['value'] += 1
            counter_label.set_text(str(counter['value']))
            
        def decrement_counter():
            counter['value'] -= 1
            counter_label.set_text(str(counter['value']))