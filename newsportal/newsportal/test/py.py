blank = 'Геоло́гия (от др.-греч. γῆ «Земля» + λόγος «учение, наука») — совокупность наук о строении Земли, её происхождении и развитии, основанных на изучении геологических процессов, вещественного состава, структуры земной коры и литосферы всеми доступными методами с привлечением данных других наук и дисциплин[1][2]. Коротко геологию можно определить как науку о составе, строении и закономерностях развития Земли и изучение её поверхности[3].  Геология прошла длительный и сложный путь развития. Круг объектов её исследования расширялся, и распространился на всю Землю (науки о Земле) и объекты Солнечной системы. В геологии предметом исследования являются геологические объекты, их свойства, закономерности строения, взаиморасположения, происхождения и развития во времени и пространстве.  В 1934—1941 годах в СССР в средней школе существовал отдельный курс «геология»[4]. После войны за возвращение геологии в школы боролись профессора В. А. Обручев, В. А. Варсанофьева[5] и другие геологи[6].'


if __name__ == "__main__":
    def cencory(value = blank , word = 'Геология'):
        w = value.split()
        for i, text in enumerate(w):
            if text == word:
                w[i] = text[0] + ('*' * (len(word) - 1))
        return w