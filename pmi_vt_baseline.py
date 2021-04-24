import time
from seleniumbase import BaseCase


class VisualLayoutTest(BaseCase):


        def test_differences_0(self):
            self.get("https://www.unsmokeyourworld.com/cr.html/")
            self.click('//button[text()="Sí"]')
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_1(self):
            self.get("https://www.unsmokeyourworld.com/cr/ayudas.html/")
            self.click('//button[text()="Sí"]')
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_2(self):
            self.get("https://www.unsmokeyourworld.com/cr/como-unsmoke.html/")
            self.click('//button[text()="Sí"]')
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_3(self):
            self.get("https://www.unsmokeyourworld.com/cr/como-unsmoke/alternativas-a-seguir-fumando-cigarrillo.html/")
            self.click('//button[text()="Sí"]')
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_4(self):
            self.get("https://www.unsmokeyourworld.com/cr/como-unsmoke/alternativas-libres-de-humo-mejor-opcion.html/")
            self.click('//button[text()="Sí"]')
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_5(self):
            self.get("https://www.unsmokeyourworld.com/cr/como-unsmoke/how-to-choose-a-smoke-free.html/")
            self.click('//button[text()="Sí"]')
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_6(self):
            self.get("https://www.unsmokeyourworld.com/cr/como-unsmoke/por-que-lanzar-esta-campana-ahora.html/")
            self.click('//button[text()="Sí"]')
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_7(self):
            self.get("https://www.unsmokeyourworld.com/cr/como-unsmoke/por-que-phillip-morris-international-lanzo-unsmoke-your-world.html/")
            self.click('//button[text()="Sí"]')
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_8(self):
            self.get("https://www.unsmokeyourworld.com/cr/como-unsmoke/que-quiere-decir-unsmoke.html/")
            self.click('//button[text()="Sí"]')
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_9(self):
            self.get("https://www.unsmokeyourworld.com/cr/como-unsmoke/quit-aids.html/")
            self.click('//button[text()="Sí"]')
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_10(self):
            self.get("https://www.unsmokeyourworld.com/cr/como-unsmoke/regulacion-alternativa-libre-de-humo.html/")
            self.click('//button[text()="Sí"]')
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_11(self):
            self.get("https://www.unsmokeyourworld.com/cr/legal.html/")
            self.click('//button[text()="Sí"]')
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_12(self):
            self.get("https://www.unsmokeyourworld.com/cr/regulation-matters.html/")
            self.click('//button[text()="Sí"]')
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_13(self):
            self.get("https://www.unsmokeyourworld.com/cr/regulation-matters/el-derecho-a-saber.html/")
            self.click('//button[text()="Sí"]')
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_14(self):
            self.get("https://www.unsmokeyourworld.com/en/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_15(self):
            self.get("https://www.unsmokeyourworld.com/en/be-heard.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_16(self):
            self.get("https://www.unsmokeyourworld.com/en/features.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_17(self):
            self.get("https://www.unsmokeyourworld.com/en/features/bulgarians-prove-their-passion-unsmoking.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_18(self):
            self.get("https://www.unsmokeyourworld.com/en/features/choice.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_19(self):
            self.get("https://www.unsmokeyourworld.com/en/features/could-unsmoking-boost-your-social-life.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_20(self):
            self.get("https://www.unsmokeyourworld.com/en/features/how-does-smoking-affect-relationships.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_21(self):
            self.get("https://www.unsmokeyourworld.com/en/features/pmi-wants-to-unsmoke-canada.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_22(self):
            self.get("https://www.unsmokeyourworld.com/en/features/representing-unsmoke-at-canada-pride.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_23(self):
            self.get("https://www.unsmokeyourworld.com/en/features/smokers-in-the-dark-over-alternatives-to-smoking-cigarettes.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_24(self):
            self.get("https://www.unsmokeyourworld.com/en/features/south-africa-joins-the-unsmoke-movement.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_25(self):
            self.get("https://www.unsmokeyourworld.com/en/features/supporting-macro-change.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_26(self):
            self.get("https://www.unsmokeyourworld.com/en/features/uk-smoking-rates-constituency.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_27(self):
            self.get("https://www.unsmokeyourworld.com/en/features/uk-smoking-rates-constituency1.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_28(self):
            self.get("https://www.unsmokeyourworld.com/en/features/unsmoke-around-the-world.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_29(self):
            self.get("https://www.unsmokeyourworld.com/en/features/unsmoke-joins-the-urban-dictionary.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_30(self):
            self.get("https://www.unsmokeyourworld.com/en/features/unsmoking-local-governments.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_31(self):
            self.get("https://www.unsmokeyourworld.com/en/features/unsmoking-portugals-forests.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_32(self):
            self.get("https://www.unsmokeyourworld.com/en/features/unsmoking-the-belgrade-business-run.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_33(self):
            self.get("https://www.unsmokeyourworld.com/en/features/unsmoking-the-world--together.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_34(self):
            self.get("https://www.unsmokeyourworld.com/en/learn-the-science.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_35(self):
            self.get("https://www.unsmokeyourworld.com/en/legal.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_36(self):
            self.get("https://www.unsmokeyourworld.com/en/news.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_37(self):
            self.get("https://www.unsmokeyourworld.com/en/news/bulgarians-prove-their-passion-unsmoking.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_38(self):
            self.get("https://www.unsmokeyourworld.com/en/news/could-unsmoking-boost-your-social-life.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_39(self):
            self.get("https://www.unsmokeyourworld.com/en/news/how-does-smoking-affect-relationships.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_40(self):
            self.get("https://www.unsmokeyourworld.com/en/news/pmi-wants-to-unsmoke-canada.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_41(self):
            self.get("https://www.unsmokeyourworld.com/en/news/representing-unsmoke-at-canada-pride.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_42(self):
            self.get("https://www.unsmokeyourworld.com/en/news/smokers-in-the-dark-over-alternatives-to-smoking-cigarettes.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_43(self):
            self.get("https://www.unsmokeyourworld.com/en/news/south-africa-joins-the-unsmoke-movement.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_44(self):
            self.get("https://www.unsmokeyourworld.com/en/news/uk-smoking-rates-constituency.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_45(self):
            self.get("https://www.unsmokeyourworld.com/en/news/unsmoke-around-the-world.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_46(self):
            self.get("https://www.unsmokeyourworld.com/en/news/unsmoke-joins-the-urban-dictionary.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_47(self):
            self.get("https://www.unsmokeyourworld.com/en/news/unsmoke-sarajevo.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_48(self):
            self.get("https://www.unsmokeyourworld.com/en/news/unsmoking-local-governments.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_49(self):
            self.get("https://www.unsmokeyourworld.com/en/news/unsmoking-portugals-forests.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_50(self):
            self.get("https://www.unsmokeyourworld.com/en/news/unsmoking-the-belgrade-business-run.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_51(self):
            self.get("https://www.unsmokeyourworld.com/en/news/unsmoking-the-world--together.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_52(self):
            self.get("https://www.unsmokeyourworld.com/en/quit-aids.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_53(self):
            self.get("https://www.unsmokeyourworld.com/en/ways-to-unsmoke.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_54(self):
            self.get("https://www.unsmokeyourworld.com/en/ways-to-unsmoke/be-inspired.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_55(self):
            self.get("https://www.unsmokeyourworld.com/en/ways-to-unsmoke/learn-the-science.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_56(self):
            self.get("https://www.unsmokeyourworld.com/es.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_57(self):
            self.get("https://www.unsmokeyourworld.com/es/ayudas.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_58(self):
            self.get("https://www.unsmokeyourworld.com/es/como-unsmoke.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_59(self):
            self.get("https://www.unsmokeyourworld.com/es/como-unsmoke/descubre-lo-que-dice-la-ciencia.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_60(self):
            self.get("https://www.unsmokeyourworld.com/es/como-unsmoke/obten-inspiracion.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_61(self):
            self.get("https://www.unsmokeyourworld.com/es/involucrate.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_62(self):
            self.get("https://www.unsmokeyourworld.com/es/legal.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_63(self):
            self.get("https://www.unsmokeyourworld.com/es/news.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_64(self):
            self.get("https://www.unsmokeyourworld.com/es/news/representing-unsmoke-at-canada-pride.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_65(self):
            self.get("https://www.unsmokeyourworld.com/es/news/south-africa-joins-the-unsmoke-movement.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_66(self):
            self.get("https://www.unsmokeyourworld.com/es/news/unsmoke-around-the-world.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            
        def test_differences_67(self):
            self.get("https://www.unsmokeyourworld.com/es/news/unsmoking-the-world--together.html/")
            self.check_window(name="unsmokeyourworld", baseline=True)
            