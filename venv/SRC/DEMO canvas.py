import kivy



#class Canvas(App):
 #   def build(self):


if __name__ == '__main__':
    try:
        Canvas().run()
    except:
        import pdb; pdb.post_mortem();
        raise