trueboard = {'1a': '', '1b': '', '1c': '', '1d': '', '1e': '', '1f': '', '1g': '', '1h': '',
'2a': '', '2b': '', '2c': '', '2d': '', '2e': '', '2f': '', '2g': '', '2h': '',
'3a': '', '3b': '', '3c': '', '3d': '', '3e': '', '3f': '', '3g': '', '3h': '',
'4a': '', '4b': '', '4c': '', '4d': '', '4e': '', '4f': '', '4g': '', '4h': '',
'5a': '', '5b': '', '5c': '', '5d': '', '5e': '', '5f': '', '5g': '', '5h': '',
'6a': '', '6b': '', '6c': '', '6d': '', '6e': '', '6f': '', '6g': '', '6h': '',
'7a': '', '7b': '', '7c': '', '7d': '', '7e': '', '7f': '', '7g': '', '7h': '',
'8a': '', '8b': '', '8c': '', '8d': '', '8e': '', '8f': '', '8g': '', '8h': '',}

testboard = {'1a': 'wking', '1b': '', '1c': '', '1d': '', '1e': '', '1f': '', '1g': '', '1h': '',
'2a': '', '2b': '', '2c': '', '2d': '', '2e': '', '2f': '', '2g': '', '2h': '',
'3a': '', '3b': '', '3c': '', '3d': '', '3e': '', '3f': '', '3g': '', '3h': '',
'4a': '', '4b': '', '4c': '', '4d': '', '4e': '', '4f': '', '4g': '', '4h': '',
'5a': '', '5b': '', '5c': '', '5d': '', '5e': '', '5f': '', '5g': '', '5h': '',
'6a': '', '6b': '', '6c': '', '6d': '', '6e': '', '6f': '', '6g': '', '6h': '',
'7a': '', '7b': 'bking', '7c': '', '7d': '', '7e': '', '7f': '', '7g': '', '7h': '',
'8a': 'wqueen', '8b': 'bqueen', '8c': 'wrook', '8d': '', '8e': '', '8f': '', '8g': '', '8h': '',}
        
def isValidChessBoard(board):
    squarecount = 0
    bkingcount = 0
    wkingcount = 0
    bqueencount = 0
    wqueencount = 0
    brookcount = 0
    wrookcount = 0
    bbishopcount = 0
    wbishopcount = 0
    bknightcount = 0
    wknightcount = 0
    bpawncount = 0
    wpawncount = 0
    othercount = 0
    for square in board.keys():
        if square in trueboard: #all pieces must be on a valid space from '1a' to '8h'
            squarecount=squarecount+1
    for pieces in board.values(): 
        if 'bking' in pieces:
            bkingcount = bkingcount+1
        if 'wking' in pieces:
            wkingcount = wkingcount+1
        if 'bqueen' in pieces:
            bqueencount = bqueencount+1
        if 'wqueen' in pieces:
            wqueencount = wqueencount+1        
        if 'brook' in pieces:
            brookcount = brookcount+1
        if 'wrook' in pieces:
            wrookcount = wrookcount+1
        if 'bbishop' in pieces:
            bbishopcount = bbishopcount+1
        if 'wbishop' in pieces:
            wbishopcount = wbishopcount+1
        if 'bknight' in pieces:
            bknightcount = bknightcount+1
        if 'wknight' in pieces:
            wknightcount = wknightcount+1
        if 'bpawn' in pieces:
            bpawncount = bpawncount+1
        if 'wpan' in pieces:
            wpawncount = wpawncount+1  
        if not(pieces.startswith('w') or pieces.startswith('b') or pieces==''): #any square not occupied by a b/w chess piece is empty
            othercount = othercount+1
    if squarecount == 64 and bkingcount == 1 and wkingcount == 1 and bqueencount <= 1 and wqueencount <= 1 and brookcount <= 2 and wrookcount <= 2\
    and bbishopcount <= 2 and wbishopcount <= 2 and bknightcount <= 2 and wknightcount <= 2 and bpawncount <= 8 and wpawncount <= 8 and othercount == 0:
        print ('True')
    else:
        print ('False')


isValidChessBoard(testboard)
