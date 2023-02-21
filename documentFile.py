import aspose.words as aw
import gameFile


doc = aw.Document()
builder = aw.DocumentBuilder(doc)

def insertTask7():

    builder.write("This is a overview of wins, losses and remis for the StockFish: ")

    #TASK 7
    counts = [0,0,0]
    gameFile.readChessWins(counts)

    table = builder.start_table()
    # insert cell 
    builder.insert_cell()
    table.auto_fit(aw.tables.AutoFitBehavior.AUTO_FIT_TO_CONTENTS)

    # set formatting and add text
    builder.cell_format.vertical_alignment = aw.tables.CellVerticalAlignment.CENTER
    builder.write("Wins ")

    # insert cell
    builder.insert_cell()
    builder.write("Lose")

    builder.insert_cell()
    builder.write("Remis")

    # end row
    builder.end_row()

    # insert another cell in the next row
    builder.insert_cell()

    # format row if required
    builder.row_format.height = 100
    builder.row_format.height_rule = aw.HeightRule.EXACTLY

    # format cell and add text
    builder.cell_format.orientation = aw.TextOrientation.HORIZONTAL
    builder.writeln(str(counts[0]))

    # insert another cell, set formatting and add text
    builder.insert_cell()
    builder.cell_format.orientation = aw.TextOrientation.HORIZONTAL
    builder.writeln(str(counts[1]))

    builder.insert_cell()
    builder.cell_format.orientation = aw.TextOrientation.HORIZONTAL
    builder.writeln(str(counts[2]))

    # end row
    builder.end_row()

    # end table
    builder.end_table()

#END OF TASK 7

#TASK 8 
listOfMoves = gameFile.readNumberOfMovesGames()
listOfMoves.sort(reverse = True)
print(listOfMoves)


insertTask7()
doc.save("test.docx")