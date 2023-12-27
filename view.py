import datetime
import io
from datetime import date

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from urllib.request import urlopen, Request

from io import BytesIO
# import tkinter.font as font
#
# from dateutil.utils import today
#
# from models_new import Fridge, Item


class View(Tk):
    frame_stack = []
    FONT1 = "Times 20 italic bold"
    FONT2 = "Times 20 bold"
    FONT3 = "Times 12 bold"
    FONT4 = "Times 14 bold"
    FONT5 = "Times 16 bold"

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.minsize(width=800, height=500)
        self.maxsize(width=800, height=500)
        self.title('Smart Fridge System')

        self.geometry('800x500')
        self.root = ttk.Frame(self, name='root')
        self.root.grid(column=0, row=0, sticky='NSEW')
        # self.root.grid_propagate(0)
        # self.frame = Frame(self.root, width=600, height=400)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.quantity_val = StringVar()
        self.quantity_val.set('')
        self.date_val = StringVar()
        self.date_val.set('1')
        self.unit_var = StringVar()
        self.unit_var.set('')
        self._create_main_window()
        self.sub_cat = ''
        self.on_start()

    def main(self):
        self.mainloop()
        pass

    # photos = [PhotoImage(file="images/home.png"), PhotoImage(file="images/back.png")]
    def new_date(self, *args):
        if not args:
            # print(self.date_val.get().split(' ')[0])
            new_date = date.today() + datetime.timedelta(int(str(self.date_val.get()).split(' ')[0]))
            var = self.date_view
            # print(new_date)
            # print(type(new_date))
            var.config(text=str(date.today() + datetime.timedelta(float(str(self.date_val.get()).split(' ')[0]))))
            return str(new_date)
        else:

            c = args[0].split('-')
            c = date(int(c[0]), int(c[1]), int(c[2]))
            td = c - date.today()
            return td



    def _create_main_window(self):
        # ---------------wellcome------------------
        self.welcome = ttk.Label(self.root, background='grey', anchor="center", justify='center',
                                 text=f'Welcome,\n{self.controller.fridge.name}', font="Times 40 bold")
        self.welcome.grid(column=0, row=0, sticky='NSEW')
        set = ttk.Style()
        set.configure('my.TButton', background='gray', borderwidth=0)
        pil_image = Image.open('images/settings1.png')
        global image_settings

        image_settings = ImageTk.PhotoImage(pil_image.resize((20, 20)))
        settings_btn = Button(self.welcome, width=15, image=image_settings, background='gray', borderwidth=0, command=lambda  action=True: self.controller.open_settings(action))
        settings_btn.grid(column=0, row=0, sticky='en')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.welcome.columnconfigure(0, weight=1)
        self.welcome.rowconfigure(0, weight=1)
        # ---------------ask------------------
        self.ask_frame = self.make_aks_window(self.root)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.ask_frame.columnconfigure(0, weight=1)
        self.ask_frame.rowconfigure(0, weight=1)
        # # ---------------add_frame--------------------------------
        self.add_frame = self.make_add_window(self.root)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.add_frame.columnconfigure(0, weight=1)
        self.add_frame.rowconfigure(0, weight=1)
        # # 00---------------------fruits_vegetables----------------------------------
        # self.fruits_vegetables_frame = self.make_fruits_vegetables_window(self.root)
        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)
        # self.fruits_vegetables_frame.columnconfigure(0, weight=1)
        # self.fruits_vegetables_frame.rowconfigure(0, weight=1)
        # # 10---------------------meat_fish----------------------------------
        # self.meat_fish_frame = self.make_meat_fish_window(self.root)
        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)
        # self.meat_fish_frame.columnconfigure(0, weight=1)
        # self.meat_fish_frame.rowconfigure(0, weight=1)
        # # 20---------------------cereals_cereal_products----------------------------------
        # self.cereals_cereal_products_frame = self.make_cereals_cereal_products_window(self.root)
        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)
        # self.cereals_cereal_products_frame.columnconfigure(0, weight=1)
        # self.cereals_cereal_products_frame.rowconfigure(0, weight=1)
        #
        # # 01---------------------milk_milk_products----------------------------------
        # self.milk_milk_products_frame = self.make_milk_milk_products_window(self.root)
        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)
        # self.milk_milk_products_frame.columnconfigure(0, weight=1)
        # self.milk_milk_products_frame.rowconfigure(0, weight=1)
        # # 11---------------------oils_fats----------------------------------
        # self.oils_fats_frame = self.make_oils_fats_window(self.root)
        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)
        # self.oils_fats_frame.columnconfigure(0, weight=1)
        # self.oils_fats_frame.rowconfigure(0, weight=1)
        #
        # # 21---------------------legumes_nuts_seeds----------------------------------
        # self.legumes_nuts_seeds_frame = self.make_legumes_nuts_seeds_window(self.root)
        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)
        # self.legumes_nuts_seeds_frame.columnconfigure(0, weight=1)
        # self.legumes_nuts_seeds_frame.rowconfigure(0, weight=1)
        #
        # # 02---------------------sweets_spices----------------------------------
        # self.sweets_spices_frame = self.make_sweets_spices_window(self.root)
        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)
        # self.sweets_spices_frame.columnconfigure(0, weight=1)
        # self.sweets_spices_frame.rowconfigure(0, weight=1)
        # # 12---------------------condiments_beverages----------------------------------
        # self.condiments_beverages_frame = self.make_condiments_beverages_window(self.root)
        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)
        # self.condiments_beverages_frame.columnconfigure(0, weight=1)
        # self.condiments_beverages_frame.rowconfigure(0, weight=1)
        #
        # # 22---------------------others----------------------------------

        # ---------------------add_sub----------------------------------

        # ---------------------add_item----------------------------------
        self.add_item_frame = self.make_add_item_window(self.root)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.add_item_frame.columnconfigure(0, weight=1)
        self.add_item_frame.rowconfigure(0, weight=1)
        # ---------------------cook-------------------------------------
        self.cook_frame = self.make_cook_window(self.root)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.cook_frame.columnconfigure(0, weight=1)
        self.cook_frame.rowconfigure(0, weight=1)
        # ---------------------shopping list-----------------------------------
        self.shopping_list_frame = self.make_qr_shopping_list_window(self.root)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.shopping_list_frame.columnconfigure(0, weight=1)
        self.shopping_list_frame.rowconfigure(0, weight=1)
        # ---------------------choose_recipe-----------------------------------
        self.cook_chosen_recipe_frame = self.make_cook_chosen_window(self.root)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.cook_chosen_recipe_frame.columnconfigure(0, weight=1)
        self.cook_chosen_recipe_frame.rowconfigure(0, weight=1)
        # -------------------------initial-------------------------------
        self.initial = self.make_initial_window(self.root)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    # def remove_product(self, a):
    #     if a.widget.curselection() not in [(), '']:
    #         sel_item = self.items_products_list_box.get(a.widget.curselection())
    #         new_list = self.chosen_products.remove(sel_item)
    #         self.set_chosen(new_list)

    def clear_chosen(self):
        self.chosen_products = []
        self.items_products_list_box.delete(0, END)

    def set_chosen(self, value):
        self.items_products_list_box.delete(0, END)

        for c in value:
            self.items_products_list_box.insert(END, c)

    def set_choices(self, value):
        self.items_list_box.delete(0, END)

        for c in value:
            self.items_list_box.insert(END, c)

    def set_recipes(self, value):
        self.recipe_list_box.delete(0, END)

        for c in value:
            self.recipe_list_box.insert(END, c)

    def selected_item_str(self, a):
        if a.widget.curselection() not in [(), '']:
            sel_item = self.items_list_box.get(a.widget.curselection())
            dates = []
            try:
                data = self.controller.search_item(sel_item)
                d_data = str(data.expiry)
                dates = d_data.split('-')
                # str_date = ', '.join(date)
                # print(str_date)
                # print(datetime.date(str_date))
                # print(datetime.date(date))
                # print(datetime.date(date.expiry))
            except AttributeError:
                pass
            if date(int(dates[0]), int(dates[1]), int(dates[2])) < date.today():
                self.update_btn['state'] = 'disabled'
                self.clear_btn['state'] = 'disabled'
                self.remove_btn['state'] = 'disabled'
                self.add_btn['state'] = 'disabled'
            if data.unit in ['g', 'kg']:
                self.units_entry['values'] = ('g', 'kg')
            elif data.unit in ['l', 'ml']:
                self.units_entry['values'] = ('ml', 'l')
            else:
                self.units_entry['values'] = ('count')
            self.set_values(data)

            old_date = data.expiry
            cur_date = date.today()

        self.update()

    def chosen_item_str(self, b):
        if b.widget.curselection() not in [(), '']:
            sel_item = self.items_list_box.get(b.widget.curselection())
            if sel_item not in [(), '']:
                data = self.controller.search_item(sel_item)
                no_digit_name = self.controller.remove_digits(data.name)
                if no_digit_name not in self.chosen_products:
                    self.chosen_products.append(no_digit_name)
                # self.choiceprodvar.set(self.chosen_products)
                self.set_chosen(self.chosen_products)
        # self.update()

    def chosen_product_str(self, c):
        if c.widget.curselection() not in [(), '']:
            sel_item = self.items_products_list_box.get(c.widget.curselection())
            self.chosen_products.remove(sel_item)
            self.set_chosen(self.chosen_products)
            # except ValueError:
            #     self.chosen_products = []
            #     self.set_chosen(self.chosen_products)

    #     # self.update()

    def clear_used_missed_instructions(self):
        self.recipe_ingredients_text.delete(1.0, 'end')
        # self.recipe_used_text['text'] = ''
        # self.recipe_missed_text['text'] = ''
        self.clear_chosen()
        self.recipe_description_text.delete(1.0, 'end')

    def recipe_find(self, d):
        self.clear_used_missed_instructions()
        if d.widget.curselection() not in [(), '']:
            recipe_name = self.recipe_list_box.get(d.widget.curselection())
            # print(recipe_id)
            try:
                recipe = ''
                if self.recipes_from_chosen_products:
                    for i in self.recipes_from_chosen_products:
                        if recipe_name == i.title:
                            recipe = i
                            break

                    self.controller.chosen_recipe = recipe
                    list_ingredients = []
                    for i in self.controller.chosen_recipe.ingredients:
                        ingr = self.controller.check_ingredients_not_to_by(i)

                        if ingr and i.name not in list_ingredients:
                            list_ingredients.append(i.name)

                    res = ', '.join(list_ingredients)
                    self.recipe_ingredients_text.insert(1.0, res)
                    self.recipe_description_text.delete(1.0, 'end')
                    if self.controller.chosen_recipe.image:
                        url = self.controller.chosen_recipe.image
                        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                        image_bytes = urlopen(req).read()
                        data_stream = io.BytesIO(image_bytes)
                        pil_image = Image.open(data_stream)
                        global tk_image
                        tk_image = ImageTk.PhotoImage(pil_image.resize((204, 144)))

                        self.lbl = ttk.Label(self.recipe_image_box, image=tk_image,)
                        self.lbl.grid(column=0, row=0, sticky='news')

                    if self.controller.chosen_recipe.instructions:
                        result = self.controller.remole_li(self.controller.chosen_recipe.instructions)
                        self.recipe_description_text.insert(1.0, result)
                    else:
                        self.recipe_description_text.insert(1.0, 'Sorry! No information available')
                    # self.chosen_products.remove(sel_item)
                    # self.set_chosen(self.chosen_products)
                elif self.random_recipes:
                    for i in self.random_recipes:
                        if recipe_name == i.title:
                            recipe = i
                            break
                    self.controller.chosen_recipe = recipe
                    list_ingredients = []
                    for i in self.controller.chosen_recipe.ingredients:
                        for z in self.controller.ingredients_not_to_buy:
                            if i.name not in z or z not in i.name:
                                if i.name not in list_ingredients:
                                    list_ingredients.append(i.name)
                    res = ', '.join(list_ingredients)
                    self.recipe_ingredients_text.insert(1.0, res)

                    if self.controller.chosen_recipe.image:
                        url = self.controller.chosen_recipe.image
                        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                        image_bytes = urlopen(req).read()
                        data_stream = io.BytesIO(image_bytes)
                        pil_image = Image.open(data_stream)
                        tk_image = ImageTk.PhotoImage(pil_image.resize((204, 144)))

                        self.lbl = ttk.Label(self.recipe_image_box, image=tk_image, )
                        self.lbl.grid(column=0, row=0, sticky='news')

                    self.recipe_description_text.delete(1.0, 'end')
                    if self.controller.chosen_recipe.instructions:
                        result = self.controller.remole_li(self.controller.chosen_recipe.instructions)
                        self.recipe_description_text.insert(1.0, result)
                    else:
                        self.recipe_description_text.insert(1.0, 'Sorry! No information available')

                else:
                    for i in self.controller.db.get_all_recipes(self.controller.session, self.controller.fridge.id):
                        if recipe_name == i.title:
                            recipe = i
                            break
                    # self.controller.get_recipe_by_id(recipe)
                    self.controller.chosen_recipe = recipe
                    list_ingredients = []
                    for i in self.controller.chosen_recipe.ingredients:
                        for z in self.controller.ingredients_not_to_buy:
                            if i.name not in z or z not in i.name:
                                if i.name not in list_ingredients:
                                    list_ingredients.append(i.name)
                    res = ', '.join(list_ingredients)
                    self.recipe_ingredients_text.insert(1.0, res)
                    self.recipe_description_text.delete(1.0, 'end')

                    if self.controller.chosen_recipe.image:
                        url = self.controller.chosen_recipe.image
                        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                        image_bytes = urlopen(req).read()
                        data_stream = io.BytesIO(image_bytes)
                        pil_image = Image.open(data_stream)
                        tk_image = ImageTk.PhotoImage(pil_image.resize((204, 144)))

                        self.lbl = ttk.Label(self.recipe_image_box, image=tk_image,)
                        self.lbl.grid(column=0, row=0, sticky='news')
                    if self.controller.chosen_recipe.instructions:
                        result = self.controller.remole_li(self.controller.chosen_recipe.instructions)
                        self.recipe_description_text.insert(1.0, result)
                    else:
                        self.recipe_description_text.insert(1.0, 'Sorry! No information available')


            except ValueError:
                self.chosen_products = []

    #
    # def remove_from_shopping_list(self, a):
    #     if a.widget.curselection() not in [(), '']:
    #         ingredient_name = self.shopping_list_content.get(a.widget.curselection())
    #         self.shopping.remove(ingredient_name)
    #         # self.choiceshopvar.set(self.shopping)

    def make_cook_chosen_window(self, parent):
        cook_chosen_frame = Frame(parent, name="cook chosen")
        cook_chosen_frame.grid(column=0, row=0, sticky='news')

        self.make_menu_buttons(cook_chosen_frame, 3)
        self.listbox_name = ttk.Label(cook_chosen_frame, text='R E C I P E S', font=self.FONT5,
                                      justify='center')
        self.listbox_name.grid(column=0, columnspan=3, row=1, sticky='n', pady=0)
        details_box = Frame(cook_chosen_frame)
        details_box.grid(column=0, columnspan=3, row=2, sticky='news', padx=6)
        self.choices_products = []
        choicevar = StringVar(self, value=self.choices_products, name='choicev')
        self.items_list_box = Listbox(details_box, height=5, width=35, font=self.FONT3, listvariable=choicevar, selectmode='browse')
        self.items_list_box.grid(column=0, row=0, sticky='news', padx=(0, 6), pady=(0, 6))
        self.items_list_box.bind('<<ListboxSelect>>', self.chosen_item_str)
        s = ttk.Scrollbar(details_box, orient=VERTICAL, command=self.items_list_box.yview)
        s.grid(column=0, row=0, sticky='ens', pady=(0, 6), padx=(0, 6))
        self.items_list_box['yscrollcommand'] = s.set
        self.chosen_products = []
        self.choiceprodvar = StringVar(self, value=self.chosen_products, name='choicepv')
        self.details_inner = Frame(details_box)
        self.details_inner.grid(column=1, row=0, sticky='news', pady=(0, 6), padx=(0, 6))
        self.items_products_list_box = Listbox(self.details_inner, height=4, font=self.FONT3, listvariable=self.choiceprodvar,
                                               selectmode='browse')
        self.items_products_list_box.grid(column=0, row=0, sticky='news')
        self.items_products_list_box.bind('<<ListboxSelect>>', self.chosen_product_str)
        s1 = ttk.Scrollbar(self.details_inner, orient=VERTICAL, command=self.items_products_list_box.yview)
        s1.grid(column=0, row=0, sticky='ens')
        self.items_products_list_box['yscrollcommand'] = s1.set
        # name_label = Listbox(details_box, width=20, height=5)
        # name_label.grid(column=0, row=0, sticky='news')

        buttons_box = Frame(details_box)
        buttons_box.grid(column=2, row=0, sticky='e', padx=(0, 6))
        # sb = ttk.Style()
        # sb.configure('my.TButton', font=('Helvetica', 12, 'bold'), justify="center",)
        # self.remove_item_btn = ttk.Button(buttons_box, text='remove item',
        #                                   command=self.remove_product)
        # self.remove_item_btn.grid(column=0, row=3, sticky='news')
        self.clear_list_btn = ttk.Button(self.details_inner, text='CLEAR', style='my.TButton', command=self.clear_chosen)
        self.clear_list_btn.grid(column=0, row=2, sticky='news', pady=(3, 0))
        self.generate_btn = ttk.Button(buttons_box, text='GET RECIPES', style='my.TButton',
                                       command=lambda action='generate': self.controller.recipe_action_buttons(action))
        self.generate_btn.grid(column=0, row=0, sticky='news', ipady=3, ipadx=4, pady=(0, 3))
        self.random_btn = ttk.Button(buttons_box, text='RANDOM RECIPES', style='my.TButton',
                                     command=lambda action='random': self.controller.recipe_action_buttons(action))
        self.random_btn.grid(column=0, row=1, sticky='news', ipady=4, ipadx=4, pady=(0, 3))
        self.favourites_btn = ttk.Button(buttons_box, text='FAVOURITE RECIPES', style='my.TButton',
                                         command=lambda action='favourites': self.controller.recipe_action_buttons(
                                             action))
        self.favourites_btn.grid(column=0, row=2, sticky='news', ipady=4, ipadx=4)
        self.get_shopping_list_btn = ttk.Button(buttons_box, text='GET\nSHOPPING\nLIST', style='my.TButton',
                                                command=lambda
                                                    action='get_shopping_list': self.controller.recipe_action_buttons(
                                                    action))
        self.get_shopping_list_btn.grid(column=1, row=0, rowspan=3, sticky='nws', padx=(8, 6), ipadx=12)

        recipes_box = Frame(cook_chosen_frame)
        recipes_box.grid(column=0, columnspan=3, row=3, sticky='news', padx=(0, 6))
        self.add_to_favourites_btn = ttk.Button(recipes_box, text='ADD TO\nFAVOURITES', style='my.TButton',
                                                command=lambda
                                                    action='add_favourites': self.controller.recipe_action_buttons(
                                                    action))
        self.add_to_favourites_btn.grid(column=1, row=1, sticky='news', padx=(1, 0), ipadx=6, pady=(0, 6),)
        self.recipes_from_chosen_products = []
        self.random_recipes = []
        # self.favourites_recipes = []
        self.shopping_list_l = []
        # choicerecipes = StringVar(self, value=self.controller.db.get_all_recipes(self.controller.session, self.controller.fridge.id), name='choicer')
        choicerecipes = StringVar(self, value=self.recipes_from_chosen_products, name='choicer')
        self.recipe_list_box = Listbox(recipes_box, height=4, width=78, font=self.FONT3, listvariable=choicerecipes, selectmode='browse')
        self.recipe_list_box.grid(column=0, row=1, sticky='news', padx=6, pady=(0, 6), ipadx=6)
        self.recipe_list_box.bind('<<ListboxSelect>>', self.recipe_find)
        sr = ttk.Scrollbar(recipes_box, orient=VERTICAL, command=self.recipe_list_box.yview)
        sr.grid(column=0, row=1, sticky='ens', pady=(0, 6))
        self.recipe_list_box['yscrollcommand'] = sr.set
        self.recipe_ingredients_box = Frame(recipes_box)
        self.recipe_ingredients_box.grid(column=0, columnspan=4, row=3, sticky='news', padx=6, pady=(0, 6))
        self.recipe_ingredients_label = ttk.Label(self.recipe_ingredients_box, font=self.FONT3, text='INGREDIENTS:', width=14)
        self.recipe_ingredients_label.grid(column=0, row=0, sticky='nw')
        self.recipe_ingredients_text = Text(self.recipe_ingredients_box, font=self.FONT3, width=62, height=2, wrap='word')
        self.recipe_ingredients_text.grid(column=1, row=0, sticky='news', padx=(2, 2), ipadx=7)
        sri = ttk.Scrollbar(self.recipe_ingredients_box, orient=VERTICAL, command=self.recipe_ingredients_text.yview)
        sri.grid(column=2, row=0, sticky='ens')
        self.recipe_ingredients_text['yscrollcommand'] = sri.set

        self.add_to_shopping_btn = ttk.Button(self.recipe_ingredients_box, text='ADD TO\nSHOPPING LIST', style='my.TButton',
                                              command=lambda
                                                  action='shopping_list': self.controller.recipe_action_buttons(action))
        self.add_to_shopping_btn.grid(column=3, row=0, sticky='news', padx=(3, 0))

        recipe_details_box = Frame(recipes_box)
        recipe_details_box.grid(column=0, columnspan=4, row=4, sticky='news', padx=6, pady=(0, 6))
        self.recipe_image_box = Frame(recipe_details_box)
        self.recipe_image_box.grid(column=2, row=2, sticky='news')
        # global ni
        global img
        # ni = PhotoImage(file='images/jb-no-photo__24078.jpg')
        img = ImageTk.PhotoImage(Image.open('images/jb-no-photo__24078.jpg'))
        self.lbl = Label(self.recipe_image_box, image=img, width=204, height=144)
        self.lbl.grid(column=0, row=0, sticky='news', padx=(4, 0))
        self.recipe_description_text = Text(recipe_details_box, font=self.FONT3, width=65, height=8, wrap='word')
        self.recipe_description_text.grid(column=0, row=2, sticky='news', ipadx=22)
        srr = ttk.Scrollbar(recipe_details_box, orient=VERTICAL, command=self.recipe_description_text.yview)
        srr.grid(column=1, row=2, sticky='ens')
        self.recipe_description_text['yscrollcommand'] = srr.set

        return cook_chosen_frame

    def make_qr_shopping_list_window(self, parent):
        shopping_list_frame = Frame(parent, name="shopping list")
        shopping_list_frame.grid(column=0, row=0, sticky='news')

        shopping_list_frame.columnconfigure(0, weight=1)
        shopping_list_frame.rowconfigure(0, weight=1)
        try:
            nm = self.sub_cat
        except AttributeError:
            nm = ''
        self.make_menu_buttons(shopping_list_frame, 2, nm)
        self.left_box = Frame(shopping_list_frame)
        self.left_box.grid(column=0, columnspan=2, row=1, sticky='news', padx=(6, 0), pady=(0, 6))
        self.left_box.columnconfigure(0, weight=1)
        self.left_box.rowconfigure(0, minsize=420, weight=1)
        self.inner_left_box = Frame(self.left_box)
        self.inner_left_box.grid(column=0, row=0, sticky='news')
        self.right_box = Frame(shopping_list_frame, background='gray')
        self.right_box.grid(column=2, row=1, sticky='news', padx=(0, 6), pady=(0, 6))
        self.right_box.columnconfigure(0, weight=1)
        self.right_box.rowconfigure(0, weight=1)
        global imge
        imge = PhotoImage(file='data.gif')
        self.label_qr = Label(self.right_box, image=imge)
        self.label_qr.grid(column=0, columnspan=2, row=0, sticky='s')
        # sq = ttk.Style()
        # sq.configure('my.TButton', font=('Helvetica', 14, 'bold'), justify="center", )

        self.clear_shopping_list_btn = ttk.Button(self.right_box, text='Clear\nShopping List', style='my.TButton',
                                              command=self.controller.clear_shopping_list)
        self.clear_shopping_list_btn.grid(column=0, row=1, ipadx=12, padx=(0, 6), pady=(6))
        self.continue_shopping_btn = ttk.Button(self.right_box, text='Continue\nShopping', style='my.TButton',
                                            command=self.fall_back_under)
        self.continue_shopping_btn.grid(column=1, row=1, ipadx=12)
        self.remove_from_fridge_cook_btn = ttk.Button(self.right_box, text='COOK', style='my.TButton',
                                                  command=self.controller.remove_from_fridge_if_any)
        self.remove_from_fridge_cook_btn.grid(column=0, columnspan=2, row=2, sticky='news', ipady=52)
        self.shopping_list_title = ttk.Label(self.left_box, text='SHOPPING LIST', font=self.FONT4,
                                             justify='center', background='gray')
        self.shopping_list_title.grid(column=0, columnspan=2, row=0, sticky='n', pady=(0, 12))
        self.shopping_list_lable = ttk.Label(self.inner_left_box, font=self.FONT4,
                                             justify='center')
        self.shopping_list_lable.grid(column=0, row=0, sticky='n', pady=(0, 12))
        self.shopping = []
        # self.choiceshopvar = StringVar(self, value=self.shopping, name='choicsev')
        # self.shopping_list_content = Text(self.inner_left_box, height=4, font=('bold', 10))
        # self.shopping_list_content.grid(column=0, row=1, sticky='news')
        # sss = ttk.Scrollbar(self.inner_left_box, orient=VERTICAL, command=self.shopping_list_content.yview)
        # sss.grid(column=0, row=1, sticky='ens')
        # self.shopping_list_content['yscrollcommand'] = sss.set
        self.shopping_list_content = ttk.Label(self.inner_left_box, font=('bold', 14))
        self.shopping_list_content.grid(column=0, row=1, sticky='news', padx=(28, 18))
        self.shopping_list_content2 = ttk.Label(self.inner_left_box, font=('bold', 14))
        self.shopping_list_content2.grid(column=2, row=1, sticky='news', padx=18)
        # self.mail_box_l = ttk.Frame(self.left_box)
        # self.mail_box_l.grid(column=0, row=2, sticky='news')
        users = self.controller.db.get_all_users(self.controller.session, self.controller.fridge.id)
        self.send_btn_box = ttk.Label(self.left_box, justify='center')
        self.send_btn_box.grid(column=0, columnspan=2, row=2, sticky='s')
        counter = 0
        for user in users:
            btn = ttk.Button(self.send_btn_box, text=f'Send to {user.username}', style='my.TButton',
                             command=lambda mail=user.mail: self.controller.send_mail(mail))
            btn.grid(column=counter, row=0, padx=(0, 18))
            counter += 1


        self.mail_btn_r = ttk.Button(self.send_btn_box, text='Send to', style='my.TButton',
                                     command=lambda x='': self.controller.send_mail(x))
        self.mail_btn_r.grid(column=counter, row=0)
        return shopping_list_frame

    def make_cook_window(self, parent):
        cook_frame = Frame(parent, name='cook_frame')
        cook_frame.grid(column=0, row=0, sticky='news')
        self.make_menu_buttons(cook_frame, 1)
        random_btn = Button(cook_frame, text='F A V O U R I T E S', font=('Arial', 19, 'bold'), justify='center', height=4,
                            command=lambda action='favourite': self.controller.action_buttons(action),
                            background='#f6e7b6', foreground='#163c5e',)
        random_btn.grid(column=0, columnspan=3, row=1, sticky='new', ipady=5)
        random_btn = Button(cook_frame, text='R A N D O M', font=('Arial', 19, 'bold'), justify='center', height=4,
                            command=lambda action='random': self.controller.action_buttons(action),
                            background='#d7e9cd', foreground='#163c5e',)
        random_btn.grid(column=0, columnspan=3, row=2, sticky='new', ipady=5)
        choose_btn = Button(cook_frame, text='C H O O S E', height=4, background='#fcdada', foreground='#163c5e',
                            command=lambda action='choose': self.controller.action_buttons(action),
                            font=('Arial', 19, 'bold'), justify='center')
        choose_btn.grid(column=0, columnspan=3, row=3, sticky='new', ipady=5)
        return cook_frame

    def make_add_item_window(self, parent):
        # st = ttk.Style()
        # st.configure('my.TButton', font=('bold', 14))

        add_item_frame = Frame(parent, name="add items")
        add_item_frame.grid(column=0, row=0, sticky='news')
        # add_item_frame.columnconfigure(0, weight=1)
        # add_item_frame.rowconfigure(0, weight=1)
        try:
            nm = self.sub_cat
        except AttributeError:
            nm = ''
        self.make_menu_buttons(add_item_frame, 3, nm)
        self.choices = []
        self.under_menu_frame = Frame(add_item_frame)
        self.under_menu_frame.grid(column=0, columnspan=3, row=1, sticky='news', padx=6)
        self.under_menu_frame.columnconfigure(0, weight=1)
        self.under_menu_frame.rowconfigure(0, weight=1)
        choicevar = StringVar(self, value=self.choices, name='choicev', )
        self.listbox_name = ttk.Label(self.under_menu_frame, text='PRODUCTS IN FRIDGE', font=self.FONT5,
                                      justify='center')
        self.listbox_name.grid(column=0, columnspan=4, row=1, sticky='n', pady=(0, 38))
        self.items_list_box = Listbox(self.under_menu_frame, height=15, listvariable=choicevar, selectmode='browse',
                                      width=37, font=self.FONT5)
        self.items_list_box.grid(column=0, row=2, sticky='e', padx=(4, 0), pady=(0, 12))
        self.items_list_box.bind('<<ListboxSelect>>', self.selected_item_str)

        s = ttk.Scrollbar(self.under_menu_frame, orient=VERTICAL, command=self.items_list_box.yview)
        s.grid(column=0, row=2, rowspan=1, sticky='ens', pady=(0, 12))
        self.items_list_box['yscrollcommand'] = s.set
        # self.listbox_name3 = ttk.Label(self.under_menu_frame, background='gray')
        # self.listbox_name3.grid(column=0, columnspan=4, row=4, sticky='news')
        details_box = Frame(self.under_menu_frame)
        details_box.grid(column=1, row=2, sticky='new')
        self.name_entry = ttk.Entry(details_box, width=28, font=self.FONT3)
        self.name_entry.grid(column=1, row=0, sticky='w', pady=3)
        self.name_entry.focus()


        date_entry = ttk.Spinbox(details_box, from_=1, to=365, textvariable=self.date_val, command=self.new_date,
                                 width=5, font=self.FONT3)

        date_entry.grid(column=1, row=1, sticky='e', padx=(0, 7))
        self.date_view = ttk.Label(details_box, text='', width=26, background='white', borderwidth=1, relief="groove", font=self.FONT3)
        self.date_view.grid(column=1, row=1, sticky='w', ipady=1)
        name_label = ttk.Label(details_box, text='Name:', font=self.FONT3, width=12)
        name_label.grid(column=0, row=0, sticky='w')
        date_label = ttk.Label(details_box, text=f'Expiry date:', font=self.FONT3)
        date_label.grid(column=0, row=1, sticky='w')
        q_box = Frame(details_box)
        q_box.grid(column=1, row=2, sticky='news')
        quantity_label = ttk.Label(details_box, text='Quantity:', font=self.FONT3)
        quantity_label.grid(column=0, row=2, sticky='w')
        self.quantity_entry = ttk.Spinbox(q_box, from_=1, to=10000, increment=1, textvariable=self.quantity_val, width=17, font=self.FONT3, state='disabled')
        self.quantity_entry.grid(column=0, row=0, sticky='w', padx=(0, 1))

        self.units_entry = ttk.Combobox(q_box, textvariable=self.unit_var, width=6, font=self.FONT3)
        self.units_entry['values'] = ('count', 'ml', 'l', 'g', 'kg')
        self.units_entry.grid(column=1, row=0, sticky='e', padx=(2, 0))
        self.units_entry.bind("<<ComboboxSelected>>", self.controller.change_spinbox)
        self.clear_btn = Button(details_box, text='CLEAR', font="Helvetica 12 bold",
                                    command=lambda action='clear': self.controller.item_action_buttons(action))
        self.clear_btn.grid(column=2, row=0, rowspan=3, sticky='nws', ipadx=4, padx=(6, 6))
        buttons_box = Frame(details_box)
        buttons_box.grid(column=0, columnspan=4, row=4, sticky='n')
        self.add_btn = Button(buttons_box, text='ADD', font="Helvetica 12 bold", width=12,
        # self.add_btn = Button(buttons_box, text='ADD', font="Helvetica 12 bold", width=19,
                                  command=lambda action='add': self.controller.item_action_buttons(action))
        self.add_btn.grid(column=0, row=0, sticky='we', padx=(0, 6), pady=(6, 6), ipadx=2, ipady=6)
        self.update_btn = Button(buttons_box, text='UPDATE', width=12, font="Helvetica 12 bold",
        # self.update_btn = Button(buttons_box, text='UPDATE', width=19, font="Helvetica 12 bold",
                                     command=lambda action='update': self.controller.item_action_buttons(action))
        self.update_btn.grid(column=1, row=0, sticky='we',  padx=(0, 6), ipadx=2, ipady=6)
        # self.remove_btn = Button(buttons_box, text='REMOVE', width=19, font="Helvetica 12 bold",
        #                              command=lambda action='remove': self.controller.item_action_buttons(action))
        # self.remove_btn.grid(column=0, row=1, sticky='ew', padx=(0, 6), pady=(6, 6), ipadx=2, ipady=6)
        self.del_btn = Button(buttons_box, text='DELETE', width=12, font="Helvetica 12 bold",
        # self.del_btn = Button(buttons_box, text='DELETE', width=19, font="Helvetica 12 bold",
                                  command=lambda action='delete': self.controller.item_action_buttons(action))
        self.del_btn.grid(column=2, row=0, sticky='we',  padx=(0, 6), ipadx=2, ipady=6)
        # self.del_btn.grid(column=1, row=1, sticky='we',  padx=(0, 6), ipadx=2, ipady=6)

        self.keyboard_box = Frame(details_box)
        self.keyboard_box.grid(column=0, columnspan=4, row=5, sticky='n')
        num_buttons = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', 'enter']
        name_buttons = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'space', 'enter']
        self.alpha_box = Frame(self.keyboard_box)
        self.controller.make_letter_buttons(self.alpha_box)
        self.alpha_box.grid(column=0, row=0, sticky='s', pady=(32, 0))

        return add_item_frame

    # def make_condiments_beverages_window(self, parent):
    #     condiments_beverages_frame = Frame(parent, name='condiments/ beverages')
    #     condiments_beverages_frame.grid(column=0, row=0, sticky='news')
    #     self.make_menu_buttons(condiments_beverages_frame, 1)
    #     condiments_btn = Button(condiments_beverages_frame, text='Condiments', font=('bold', 18), justify='center',
    #                             command=lambda action='condiments': self.controller.action_buttons(action))
    #     condiments_btn.grid(column=0, columnspan=3, row=1, sticky='sewn')
    #     beverages_btn = Button(condiments_beverages_frame, text='Beverages',
    #                            command=lambda action='beverages': self.controller.action_buttons(action),
    #                            font=('bold', 18), justify='center')
    #     beverages_btn.grid(column=0, columnspan=3, row=2, sticky='sewn')
    #     return condiments_beverages_frame
    #
    # def make_sweets_spices_window(self, parent):
    #     sweets_spices_frame = Frame(parent, name='sweets/ spices')
    #     sweets_spices_frame.grid(column=0, row=0, sticky='news')
    #     self.make_menu_buttons(sweets_spices_frame, 1)
    #     sweets_btn = Button(sweets_spices_frame, text='Sweets', font=('bold', 18), justify='center',
    #                         command=lambda action='sweets': self.controller.action_buttons(action))
    #     sweets_btn.grid(column=0, columnspan=3, row=1, sticky='sewn')
    #     spices_btn = Button(sweets_spices_frame, text='Spices',
    #                         command=lambda action='spices': self.controller.action_buttons(action),
    #                         font=('bold', 18), justify='center')
    #     spices_btn.grid(column=0, columnspan=3, row=2, sticky='sewn')
    #     return sweets_spices_frame
    #
    # def make_legumes_nuts_seeds_window(self, parent):
    #     legumes_nuts_seeds_frame = Frame(parent, name='legumes/ nuts/ seeds')
    #     legumes_nuts_seeds_frame.grid(column=0, row=0, sticky='news')
    #     self.make_menu_buttons(legumes_nuts_seeds_frame, 1)
    #     legumes_btn = Button(legumes_nuts_seeds_frame, text='Legumes', font=('bold', 18), justify='center',
    #                          command=lambda action='legumes': self.controller.action_buttons(action))
    #     legumes_btn.grid(column=0, columnspan=3, row=1, sticky='sewn')
    #     nuts_btn = Button(legumes_nuts_seeds_frame, text='Nuts',
    #                       command=lambda action='nuts': self.controller.action_buttons(action),
    #                       font=('bold', 18), justify='center')
    #     nuts_btn.grid(column=0, columnspan=3, row=2, sticky='sewn')
    #     seeds_btn = Button(legumes_nuts_seeds_frame, text='Seeds',
    #                        command=lambda action='seeds': self.controller.action_buttons(action),
    #                        font=('bold', 18), justify='center')
    #     seeds_btn.grid(column=0, columnspan=3, row=3, sticky='sewn')
    #     return legumes_nuts_seeds_frame
    #
    # def make_oils_fats_window(self, parent):
    #     oils_fats_frame = Frame(parent, name='oils/ fats')
    #     oils_fats_frame.grid(column=0, row=0, sticky='news')
    #     self.make_menu_buttons(oils_fats_frame, 1)
    #     oils_btn = Button(oils_fats_frame, text='Oils', font=('bold', 18), justify='center',
    #                       command=lambda action='oils': self.controller.action_buttons(action))
    #     oils_btn.grid(column=0, columnspan=3, row=1, sticky='ewn')
    #     fats_btn = Button(oils_fats_frame, text='Fats',
    #                       command=lambda action='fats': self.controller.action_buttons(action),
    #                       font=('bold', 18), justify='center')
    #     fats_btn.grid(column=0, columnspan=3, row=2, sticky='ews')
    #     return oils_fats_frame
    #
    # def make_milk_milk_products_window(self, parent):
    #     milk_milk_products_frame = Frame(parent, name='milk/ milk products')
    #     milk_milk_products_frame.grid(column=0, row=0, sticky='news')
    #     self.make_menu_buttons(milk_milk_products_frame, 1)
    #     milk_btn = Button(milk_milk_products_frame, text='Milk', font=('bold', 18), justify='center',
    #                       command=lambda action='milk': self.controller.action_buttons(action))
    #     milk_btn.grid(column=0, columnspan=3, row=1, sticky='ewn')
    #     milk_products_btn = Button(milk_milk_products_frame, text='Milk Products',
    #                                command=lambda action='milk product': self.controller.action_buttons(action),
    #                                font=('bold', 18), justify='center')
    #     milk_products_btn.grid(column=0, columnspan=3, row=2, sticky='ews')
    #     return milk_milk_products_frame
    #
    # def make_cereals_cereal_products_window(self, parent):
    #     cereals_cereal_products_frame = Frame(parent, name='cereals/ cereal products')
    #     cereals_cereal_products_frame.grid(column=0, row=0, sticky='news')
    #     self.make_menu_buttons(cereals_cereal_products_frame, 1)
    #     cereals_btn = Button(cereals_cereal_products_frame, text='Cereals', font=('bold', 18), justify='center',
    #                          command=lambda action='cereals': self.controller.action_buttons(action))
    #     cereals_btn.grid(column=0, columnspan=3, row=1, sticky='ewn')
    #     cereal_products_btn = Button(cereals_cereal_products_frame, text='Cereal Products',
    #                                  command=lambda action='cereal product': self.controller.action_buttons(action),
    #                                  font=('bold', 18), justify='center')
    #     cereal_products_btn.grid(column=0, columnspan=3, row=2, sticky='ews')
    #     return cereals_cereal_products_frame
    #
    # def make_meat_fish_window(self, parent):
    #     meat_fish_frame = Frame(parent, name='meat/ fish')
    #     meat_fish_frame.grid(column=0, row=0, sticky='news')
    #     self.make_menu_buttons(meat_fish_frame, 1)
    #     meat_btn = Button(meat_fish_frame, text='Meat', font=('bold', 18), justify='center',
    #                       command=lambda action='meat': self.controller.action_buttons(action))
    #     meat_btn.grid(column=0, columnspan=3, row=1, sticky='news')
    #     fish_btn = Button(meat_fish_frame, text='Fish',
    #                       command=lambda action='fish': self.controller.action_buttons(action),
    #                       font=('bold', 18), justify='center')
    #     fish_btn.grid(column=0, columnspan=3, row=2, sticky='news')
    #     return meat_fish_frame

    # def make_fruits_vegetables_window(self, parent):
    #     fruits_vegetables_frame = Frame(parent, name='fruits/ vegetables')
    #     fruits_vegetables_frame.grid(column=0, row=0, sticky='news')
    #     self.make_menu_buttons(fruits_vegetables_frame, 1)
    #     fruits_btn = Button(fruits_vegetables_frame, text='Fruits', font=('bold', 18), justify='center', height=7,
    #                         command=lambda action='fruits': self.controller.action_buttons(action))
    #     fruits_btn.grid(column=0, columnspan=3, row=1, sticky='news')
    #     vegs_btn = Button(fruits_vegetables_frame, text='Vegetables', height=7,
    #                       command=lambda action='vegetables': self.controller.action_buttons(action),
    #                       font=('bold', 18), justify='center')
    #     vegs_btn.grid(column=0, columnspan=3, row=2, sticky='news')
    #     return fruits_vegetables_frame

    def make_add_window(self, parent):
        add_frame = ttk.Frame(parent, name='others')
        add_frame.grid(column=0, row=0, sticky='news')

        global fruit
        fruit = PhotoImage(file='images/png products/fruits1.png')
        global vegetable
        vegetable = PhotoImage(file='images/png products/vegetables1.png')
        global cereals
        cereals = PhotoImage(file='images/png products/cereals1.png')
        global meats
        meats = PhotoImage(file='images/png products/meat1.png')
        global fishs
        fishs = PhotoImage(file='images/png products/fish1.png')
        global dairy
        dairy = PhotoImage(file='images/png products/dairy1.png')
        global oils
        oils = PhotoImage(file='images/png products/oils1.png')
        global legumes
        legumes = PhotoImage(file='images/png products/legumes1.png')
        global other
        other = PhotoImage(file='images/png products/other1.png')

        self.make_menu_buttons(add_frame, 3)
        # row1
        fruits = Button(add_frame, text='Fruits', font=('bold', 18), justify='center', image=fruit, background='white',
                        command=lambda action='fruits': self.controller.action_buttons(action))
        fruits.grid(column=0, row=1, sticky='news')
        vegetables = Button(add_frame, text='Vegetables', font=('bold', 18), justify='center', image=vegetable,
                            background='white',
                            command=lambda action='vegetables': self.controller.action_buttons(action))
        vegetables.grid(column=1, row=1, sticky='news')
        cereals_cereal_products = Button(add_frame, text='Cereals', font=('bold', 18), justify='center', image=cereals,
                                         background='white',
                                         command=lambda action='cereals': self.controller.action_buttons(action))
        cereals_cereal_products.grid(column=2, row=1, sticky='news')
        # row2
        meat = Button(add_frame, text='Meat', font=('bold', 18), justify='center', image=meats, background='white',
                      command=lambda action='meat': self.controller.action_buttons(action))
        meat.grid(column=0, row=2, sticky='news')
        fish = Button(add_frame, text='Fish', font=('bold', 18), justify='center', image=fishs, background='white',
                      command=lambda action='fish': self.controller.action_buttons(action))
        fish.grid(column=1, row=2, sticky='news')
        milk_milk_products_dairy = Button(add_frame, text='Dairy', font=('bold', 18), justify='center', image=dairy,
                                          background='white',
                                          command=lambda action='dairy': self.controller.action_buttons(action))
        milk_milk_products_dairy.grid(column=2, row=2, sticky='news')
        # row3
        oils_fats = Button(add_frame, text='Oils', font=('bold', 18), justify='center', image=oils, background='white',
                           command=lambda action='oils': self.controller.action_buttons(action))
        oils_fats.grid(column=0, row=3, sticky='news')
        legumes_nuts_seeds = Button(add_frame, text='Legumes', font=('bold', 18), justify='center', image=legumes,
                                    background='white',
                                    command=lambda action='legumes': self.controller.action_buttons(action))
        legumes_nuts_seeds.grid(column=1, row=3, sticky='news', ipadx=6)
        others = Button(add_frame, text='Others', font=('bold', 18), justify='center', image=other, background='white',
                        command=lambda action='other': self.controller.action_buttons(action))
        others.grid(column=2, row=3, sticky='news', ipadx=6)
        return add_frame

    def make_aks_window(self, parent):
        global bag
        bag = PhotoImage(file='images/bag1.png')
        global chef
        chef = PhotoImage(file='images/hat1.png')

        self.ask = ttk.Frame(parent, name='ask', )
        self.ask.grid(column=0, row=0, sticky='news')
        self.ask.columnconfigure(0, weight=1)
        self.ask.rowconfigure(0, weight=1)
        btn_add_item = Button(self.ask, text='ADD PRODUCT\n', image=bag, compound=BOTTOM, font="Times 20  bold",
                              foreground='black',
                              justify='center', command=lambda action='add': self.controller.action_buttons(action))
        btn_add_item.grid(column=0, row=0, sticky='news', )
        btn_add_item.columnconfigure(0, weight=1)
        btn_add_item.rowconfigure(0, weight=1)
        btn_cook = Button(self.ask, text='COOK RECIPE\n', image=chef, compound=BOTTOM, foreground='black',
                          command=lambda action='cook': self.controller.action_buttons(action),
                          font="Times 20  bold", justify='center', background='lightgray')
        btn_cook.grid(column=1, row=0, sticky='news', ipadx=50)
        btn_cook.columnconfigure(0, weight=1)
        btn_cook.rowconfigure(0, weight=1)
        if self.controller.expired_products:
            self.display_expired_for_deleting()
        return self.ask

    def display_expired_for_deleting(self):
        ex_pr = [x.name for x in self.controller.expired_products]
        expired = '\n'.join(ex_pr)
        # se = ttk.Style()
        # se.configure('my.TButton', font=('Times', 26, 'bold', 'italic'), justify="center")
        self.pop_expired = ttk.Button(self.ask, text=f'EXPIRED ITEMS:\n\n\n\n{expired}\n\n\n\n\nClick to DELETE from list\n\nremove from fridge', command=self.controller.delete_expired,
                                      style='my.TButton')
        self.pop_expired.grid(column=0, columnspan=2, row=0, sticky='news', ipady=220)

    def make_initial_window(self, parent, *args):
        s = ttk.Style()
        s.configure('my.TButton', font=('Helvetica', 12, 'bold'), justify="center",)
        if self.controller.fridge.name == 'Change name' or args:
            self.initial_frame = ttk.Frame(self.root)
            self.initial_frame.columnconfigure(0, weight=1)
            self.initial_frame.rowconfigure(0, weight=1)
            self.initial_frame.grid(column=0, row=0, sticky='news')
            self.initial_label = ttk.Label(self.initial_frame, text='Set Fridge', font='Times 30 bold italic',
                                           justify='center')
            self.initial_label.grid(column=0, columnspan=6, row=0, sticky='n', pady=20)
            self.initial_box = ttk.Frame(self.initial_frame, padding=(5, 5))
            self.initial_box.grid(column=0, columnspan=6, row=1, sticky='n')
            self.init_name_label = ttk.Label(self.initial_box, text="Fridge's name: ", font=('Helvetica', 14),
                                             )
            self.init_name_label.grid(column=0, row=1, sticky='n', pady=12)
            self.init_name_entry = ttk.Entry(self.initial_box, font=('Helvetica', 14))
            self.init_name_entry.grid(column=1, columnspan=3, row=1, sticky='ew')


            self.first_user_label = ttk.Label(self.initial_box, text='User: ', font=('Helvetica', 12))
            self.first_user_label.grid(column=0, row=3, pady=5, sticky='en')
            self.first_user_entry = ttk.Entry(self.initial_box, font=('Helvetica', 12))
            self.first_user_entry.grid(column=1, row=3, padx=(0, 30))
            self.first_user_mail = ttk.Label(self.initial_box, text="e-mail: ", font=('Helvetica', 12))
            self.first_user_mail.grid(column=2, row=3, padx=5)
            self.first_user_mail_entry = ttk.Entry(self.initial_box, font=('Helvetica', 12))
            self.first_user_mail_entry.grid(column=3, row=3)
            self.update_first_user = Button(self.initial_box, text='UPDATE', foreground='white', background='blue',
                                            font=('Helvetica', 8, 'bold'), command=lambda x=0: self.controller.update_user(x))

            self.update_first_user.grid(column=4, row=3, sticky='ew', padx=6)
            self.delete_first_user = Button(self.initial_box, text='DELETE', foreground='white', background='red',
                                            font=('Helvetica', 8, 'bold'), command=lambda x=0: self.controller.delete_user(x))

            self.delete_first_user.grid(column=5, row=3, sticky='ew')
            self.clean_row = 4
            self.sec_user_label = ttk.Label(self.initial_box, text='User: ', font=('Helvetica', 12))
            self.sec_user_entry = ttk.Entry(self.initial_box, font=('Helvetica', 12))
            self.sec_user_mail = ttk.Label(self.initial_box, text="e-mail: ", font=('Helvetica', 12))
            self.sec_user_mail_entry = ttk.Entry(self.initial_box, font=('Helvetica', 12))
            self.update_sec_user = Button(self.initial_box, text='UPDATE', foreground='white', background='blue',
                                            font=('Helvetica', 8, 'bold'), command=lambda x=1: self.controller.update_user(x))
            self.delete_sec_user = Button(self.initial_box, text='DELETE', foreground='white', background='red',
                                            font=('Helvetica', 8, 'bold'), command=lambda x=1: self.controller.delete_user(x))
            self.third_user_label = ttk.Label(self.initial_box, text='User: ', font=('Helvetica', 12))
            self.third_user_entry = ttk.Entry(self.initial_box, font=('Helvetica', 12))
            self.third_user_mail = ttk.Label(self.initial_box, text="e-mail: ", font=('Helvetica', 12))
            self.third_user_mail_entry = ttk.Entry(self.initial_box, font=('Helvetica', 12))
            self.update_third_user = Button(self.initial_box, text='UPDATE', foreground='white', background='blue',
                                            font=('Helvetica', 8, 'bold'), command=lambda x=2: self.controller.update_user(x))
            self.delete_third_user = Button(self.initial_box, text='DELETE', foreground='white', background='red',
                                            font=('Helvetica', 8, 'bold'), command=lambda x=2: self.controller.delete_user(x))
            self.four_user_label = ttk.Label(self.initial_box, text='User: ', font=('Helvetica', 12))
            self.four_user_entry = ttk.Entry(self.initial_box, font=('Helvetica', 12))
            self.four_user_mail = ttk.Label(self.initial_box, text="e-mail: ", font=('Helvetica', 12))
            self.four_user_mail_entry = ttk.Entry(self.initial_box, font=('Helvetica', 12))
            self.update_four_user = Button(self.initial_box, text='UPDATE', foreground='white', background='blue',
                                            font=('Helvetica', 8, 'bold'), command=lambda x=3: self.controller.update_user(x))
            self.delete_four_user = Button(self.initial_box, text='DELETE', foreground='white', background='red',
                                            font=('Helvetica', 8, 'bold'), command=lambda x=3: self.controller.delete_user(x))

            self.fifth_user_label = ttk.Label(self.initial_box, text='User: ', font=('Helvetica', 12))
            self.fifth_user_entry = ttk.Entry(self.initial_box, font=('Helvetica', 12))
            self.fifth_user_mail = ttk.Label(self.initial_box, text="e-mail: ", font=('Helvetica', 12))
            self.fifth_user_mail_entry = ttk.Entry(self.initial_box, font=('Helvetica', 12))
            self.update_fifth_user = Button(self.initial_box, text='UPDATE', foreground='white', background='blue',
                                            font=('Helvetica', 8, 'bold'), command=lambda x=4: self.controller.update_user(x))
            self.delete_fifth_user = Button(self.initial_box, text='DELETE', foreground='white', background='red',
                                            font=('Helvetica', 8, 'bold'), command=lambda x=4: self.controller.delete_user(x))

            self.sixth_user_label = ttk.Label(self.initial_box, text='User: ', font=('Helvetica', 12))
            self.sixth_user_entry = ttk.Entry(self.initial_box, font=('Helvetica', 12))
            self.sixth_user_mail = ttk.Label(self.initial_box, text="e-mail: ", font=('Helvetica', 12))
            self.sixth_user_mail_entry = ttk.Entry(self.initial_box, font=('Helvetica', 12))
            self.update_sixth_user = Button(self.initial_box, text='UPDATE', foreground='white', background='blue',
                                            font=('Helvetica', 8, 'bold'), command=lambda x=5: self.controller.update_user(x))
            self.delete_sixth_user = Button(self.initial_box, text='DELETE', foreground='white', background='red',
                                            font=('Helvetica', 8, 'bold'), command=lambda x=5: self.controller.delete_user(x))

            self.sev_user_label = ttk.Label(self.initial_box, text='User: ', font=('Helvetica', 12))
            self.sev_user_entry = ttk.Entry(self.initial_box, font=('Helvetica', 12))
            self.sev_user_mail = ttk.Label(self.initial_box, text="e-mail: ", font=('Helvetica', 12))
            self.sev_user_mail_entry = ttk.Entry(self.initial_box, font=('Helvetica', 12))
            self.update_sev_user = Button(self.initial_box, text='UPDATE', foreground='white', background='blue',
                                            font=('Helvetica', 8, 'bold'), command=lambda x=6: self.controller.update_user(x))
            self.delete_sev_user = Button(self.initial_box, text='DELETE', foreground='white', background='red',
                                            font=('Helvetica', 8, 'bold'), command=lambda x=6: self.controller.delete_user(x))

            self.add_user_btn = Button(self.initial_box, text='ADD USER', command=self.controller.add_new_user, foreground='white',
                                           font=('Helvetica', 12, 'bold'), background='orange')
            self.add_user_btn.grid(column=4, columnspan=2, row=11, sticky='es', pady=10)
            self.submit_fridge_data_btn = Button(self.initial_box, text='SUBMIT', foreground='white', background='green',
                                                     command=self.controller.initial_data, font=('Helvetica', 12, 'bold'))
            self.submit_fridge_data_btn.grid(column=1, columnspan=3, row=10, pady=10, sticky='ews')
            self.invalid_name_message = ttk.Label(self.initial_box, text='Invalid name', justify='center', foreground='red', font=('Times', 14, 'bold'))
            self.invalid_username_message = ttk.Label(self.initial_box, text='No username', justify='center', foreground='red', font=('Times', 14, 'bold'))
            self.invalid_mail_message = ttk.Label(self.initial_box, text='Invalid email', justify='center', foreground='red', font=('Times', 14, 'bold'))

            if args:
                name = self.controller.fridge.name[:-9]
                self.init_name_entry.insert(0, name)
                all_users = self.controller.db.get_all_users(self.controller.session, self.controller.fridge.id)
                user_fields = [(self.first_user_entry, self.first_user_mail_entry),
                               (self.sec_user_entry, self.sec_user_mail_entry),
                               (self.third_user_entry, self.third_user_mail_entry),
                               (self.four_user_entry, self.four_user_mail_entry),
                               (self.fifth_user_entry, self.fifth_user_mail_entry),
                               (self.sixth_user_entry, self.sixth_user_mail_entry),
                               (self.sev_user_entry, self.sev_user_mail_entry),
                               ]
                inr_countr = 0
                for u in all_users:
                    if inr_countr > 0:
                        self.controller.add_new_user()
                    user_fields[inr_countr][0].insert(0, u.username)
                    user_fields[inr_countr][1].insert(0, u.mail)
                    inr_countr += 1
            else:
                return self.initial_frame
        else:
            return self.on_start()

    def make_menu_buttons(self, parent, colspan, *name_sub):
        home_sub_menu = Frame(parent)
        home_sub_menu.grid(column=0, row=0, sticky='wn')
        home_sub_menu.columnconfigure(0, weight=1)
        home_sub_menu.rowconfigure(0, weight=1)
        home_menu = Button(home_sub_menu, text='COOK', font="Times 16 italic bold",
                           command=lambda action='cook': self.controller.action_buttons(action))
        home_menu.grid(column=0, row=0, sticky='news')
        add_menu = Button(home_sub_menu, text='ADD', font="Times 16 italic bold",
                          command=lambda action='add': self.controller.action_buttons(action))
        add_menu.grid(column=1, row=0, sticky='news')
        # or buttons ???
        self.middle_menu_label = ttk.Label(parent)
        # self.middle_menu_label.grid(column=1, columnspan=2, row=0, sticky='news')

        back_menu = Button(parent, text='BACK', foreground='#fffeed',
                           command=self.fall_back_under, background='#163c5e', font="Times 16 italic bold")
        back_menu.grid(column=2, row=0, sticky='ne')
        # self.middle_menu_label.grid(column=1, columnspan=colspan, row=0, sticky='news')

        # fruit_veg_menu = Button(parent, text='fruits\nvegetables',
        #                         command=lambda action='fruits_vegetables': self.controller.action_buttons(action))
        # fruit_veg_menu.grid(column=1, row=0, sticky='news')
        # meat_fish_menu = Button(parent, text='meat\nfish',
        #                         command=lambda action='meat_fish': self.controller.action_buttons(action))
        # meat_fish_menu.grid(column=2, row=0, sticky='news')
        # cer_cer_prod_menu = Button(parent, text='cereals\ncereal\nproducts',
        #                         command=lambda action='cereals_cereal_products': self.controller.action_buttons(action))
        # cer_cer_prod_menu.grid(column=3, row=0, sticky='news')
        # milk_milk_prod_menu = Button(parent, text='milk\nmilk\nproducts',
        #                         command=lambda action='milk_milk_products': self.controller.action_buttons(action))
        # milk_milk_prod_menu.grid(column=4, row=0, sticky='news')
        # oils_fats_menu = Button(parent, text='oils\nfats',
        #                         command=lambda action='oils_fats': self.controller.action_buttons(action))
        # oils_fats_menu.grid(column=5, row=0, sticky='news')
        # legumes_nuts_seeds_menu = Button(parent, text='legumes\nnuts\nseeds',
        #                         command=lambda action='legumes_nuts_seeds': self.controller.action_buttons(action))
        # legumes_nuts_seeds_menu.grid(column=6, row=0, sticky='news')
        # sweets_spices_menu = Button(parent, text='sweets\nspices',
        #                         command=lambda action='sweets_spices': self.controller.action_buttons(action))
        # sweets_spices_menu.grid(column=1, row=0, sticky='news')
        # condiments_beverages_menu = Button(parent, text='condiments\nbeverages',
        #                         command=lambda action='condiments_beverages': self.controller.action_buttons(action))
        # condiments_beverages_menu.grid(column=1, row=0, sticky='news')
        # others_menu = Button(parent, text='fruits\nvegetables',
        #                         command=lambda action='fruits_vegetables': self.controller.action_buttons(action))
        # others_menu.grid(column=1, row=0, sticky='news')
        # back_menu = Button(parent, text='back',
        #                    command=self.fall_back_under, background='gray',  font="Times 20 italic bold")
        # back_menu.grid(column=2, columnspan=colspan, row=0, sticky='ne')

    def on_start(self):
        if self.controller.fridge.name != 'Change name':
            self.raise_above_all(self.welcome, '')
            self.frame_stack.pop()
            # with delay 2s
            self.after(5000, lambda: self.raise_above_all(self.ask_frame, ''))
            # without delay for testing
            # self.after(0000, lambda: self.raise_above_all(self.ask_frame, ''))
        else:
            self.raise_above_all(self.initial, '')

    def raise_above_all(self, win1, action):
        if win1 == self.ask_frame and self.controller.wait:
            try:
                self.initial.lift()
            except AttributeError:
                pass
        else:
            win1.lift()
            if self.frame_stack and win1 != self.frame_stack[0]:
                if win1 != self.frame_stack[-1]:
                    self.frame_stack.append(win1)
            else:
                self.frame_stack.clear()
                self.frame_stack.append(win1)
            self.sub_cat = action
            if self.sub_cat == 'random':
                self.clear_used_missed_instructions()
                self.random_recipes = self.controller.get_random_recipes()
                self.set_recipes(self.random_recipes)
            elif self.sub_cat == 'favourite':
                self.clear_used_missed_instructions()
                self.controller.chosen_recipe = None
                self.set_recipes(self.controller.db.get_all_recipes(self.controller.session, self.controller.fridge.id))
                self.random_recipes = []
            elif self.sub_cat == 'choose':
                self.clear_used_missed_instructions()
                self.controller.chosen_recipe = None
                self.set_recipes([])
                self.random_recipes = []
            self.middle_menu_label.config(text=self.sub_cat)
            self.set_values()

    def fall_back_under(self):
        if len(self.frame_stack) > 1:
            self.frame_stack.pop()
            self.raise_above_all(self.frame_stack[-1], '')

    def set_values(self, *args):
        if not args:
            self.quantity_val.set('')
            self.date_val.set('1')
            self.date_view['text'] = self.new_date()
            self.name_entry.delete(0, END)
            self.name_entry.insert(0, '')
            self.units_entry['values'] = ('count', 'ml', 'l', 'g', 'kg')
            self.unit_var.set('')
            self.units_entry.set('')
            self.name_entry.focus()
            self.quantity_entry['state'] = 'disabled'
        else:
            data = args[0]
            self.unit_var.set(data.unit)
            self.controller.change_spinbox(data)
            self.quantity_val.set(data.amount)
            self.date_view['text'] = data.expiry
            self.date_val.set(self.new_date(data.expiry))
            self.name_entry.delete(0, END)
            self.name_entry.insert(0, data.name)

    def get_values(self):
        name_item = self.name_entry.get()
        quantity = self.quantity_val.get()
        unit = self.unit_var.get()
        expiry_date = self.new_date()
        sub_category = self.sub_cat
        if unit and quantity:
            n_quantity, n_unit = self.controller.make_unit(quantity, unit)
            return name_item, n_quantity, n_unit, expiry_date, sub_category
        else:
            return name_item, quantity, unit, expiry_date, sub_category

    def enable_buttons(self):
        self.add_btn['state'] = 'normal'
        self.update_btn['state'] = 'normal'
        self.remove_btn['state'] = 'normal'
        self.clear_btn['state'] = 'normal'
        self.del_btn['state'] = 'normal'
