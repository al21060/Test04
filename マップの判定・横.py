#行数 H , 列数 W の盤面があり、盤面の各マスには文字が 1 つだけ書かれています。
#盤面が与えられるので、「左右のマスが "#" 」であるようなマスの座標を全て出力してください。

#ただし、左端のマスの場合は「右のマスが "#" 」であれば、右端のマスの場合は「左のマスが "#" 」であれば条件を満たすものとします。

#なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
#下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

Row,Col=map(int,input().split())#行と列の数値を格納
Board = [list(input()) for _ in range(Row)]#盤面の状態を格納
for i in range(Row):
    
    for j in range(Col):
        if j==0:#右隣判別
            if Board[i][j+1]=="#":
                print(i,j)
            
        elif j==Col-1:#左隣判別
            if Board[i][j-1]=="#":
                print(i,j)
        else:#左右判別
            if Board[i][j+1]=="#" and Board[i][j-1]=="#":
                print(i,j)