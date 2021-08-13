x = 0
        y = 0
        lf_num = 1
        inf = ''
        Name1 = None
        for c  in range (0, 1):
                try:
                        inf = lf[1]
                except:
                        inf = None
                item = self.tableWidget.item(x, y)
                item.setText(_translate("MainWindow", Name1))
                lf_num += 1
                y += 1
                if y == 2:
                        y = 0
                        x += 1
