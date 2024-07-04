#空隙を含むイオン伝導体の成形体を迷路に見立てて、電場をかけたときのイオンの動きをシミュレーション

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as colors
from matplotlib.artist import Artist 
import random
import copy
import scipy.stats as st

# 迷路のサイズ
maze_size = (50, 50)

# イオンの動き方を定義
moves = [(0, 1), (1, 0), (-1, 0), (0, 0)] # 上、右、左、静止

# カスタムカラーマップの作成
cmap = colors.ListedColormap(['white', 'saddlebrown'])

#屈曲度リスト作成
tortuosity = []

count = 0

# アニメーション更新関数
def update(ims,step):
    # 終了判定
    terminate = False
    # イオンの次の位置を決定
    # 壁の最も上端まで来たら静止
    if pacman_position[1] == 48:
        terminate = True
        move = moves[3]
    # 上のブロックが空隙でないなら必ず上に移動
    elif maze[pacman_position[1]+1, pacman_position[0]] == 0:
        move = moves[0]
    # 上のブロックが空隙かつ左右のどちらかが空隙ならもう片方に移動。
    elif maze[pacman_position[1], pacman_position[0]-1] == 1 and maze[pacman_position[1], pacman_position[0]+1] == 0: 
        move = moves[1]
    elif maze[pacman_position[1], pacman_position[0]+1] == 1 and maze[pacman_position[1], pacman_position[0]-1] == 0: 
        move = moves[2]
    elif maze[pacman_position[1], pacman_position[0]-1] == 1 and maze[pacman_position[1], pacman_position[0]+1] == 1:
        terminate = True
        move = moves[3]
    # 上のブロックが空隙かつ左右が両方空隙でないなら左右のどちらかに移動
    else: 
        move = random.choice([moves[1], moves[2]])
    new_position = [pacman_position[0] + move[0], pacman_position[1] + move[1]]
    # 新しい位置が空隙もしくは壁でなければ移動する
    if maze[new_position[1], new_position[0]] == 0:
        pacman_position[0], pacman_position[1] = new_position
    # 現在の位置をプロット
    ax.scatter(*pacman_position, color='red')
    ax.set_title(f'step:{step}')
    # グラフのデータをimsにappend
    ims.append(ax.get_children())
    return terminate
    
#シミュレーションは入力したステップ数だけ繰り返す
print("How many steps will you simulate?")
times = int(input())
print("What fraction of porosity will you use? (Answer in a range from 0 to 1) (Recommended: 0.3 or below)")
porosity = float(input())
while count < times:
    # 迷路の生成 
    maze = np.random.choice([0, 1], size=maze_size, p=[1-porosity, porosity])
    maze[0,:] = 0
    maze[:, 0] = maze[:, -1] = maze[-1,:] = 1
    # イオンの初期位置：底の真ん中とした
    pacman_position = [25, 0]
    ims = []
    # 描画の準備
    fig,ax = plt.subplots(figsize=(5,5))
    # 背景を描画
    ax.imshow(maze, cmap=cmap)
    ax.set(xlim=(-0.5, maze_size[0] - 0.5), ylim=(-0.5, maze_size[1] - 0.5))
    # 初期座標をplot
    ax.scatter(*pacman_position, color='red')
    ims.append(ax.get_children())
    s = 0
    # もしも袋小路にとらわれた場合whileだと永遠に回り続けるためforで実装
    for i in range(100):
        # imsにプロットのデータをためていく
        # 終了判定がtrueならbreak
        if update(ims,i) == True:
            s = i
            break

    #袋小路に閉じ込められなければ伝導ブロック数をファイルに保存
    if pacman_position[1] == 48:
        count += 1
        tortuosity.append(s/48)
    plt.close()
    print(s/48, count)
    
#屈曲度の平均値を出す
average = sum(tortuosity)/len(tortuosity)
Character1 = "Average of tortuosity:"
print(Character1,average)
#屈曲度の信頼区間を出す
range = st.norm.interval(0.95, loc=average, scale=st.sem(tortuosity))
Character2 = "95% Confidence interval:"
print(Character2,range)
# アニメーションの生成
ani = animation.ArtistAnimation(fig, ims, interval=200)

# アニメーションの生成
#ani = animation.FuncAnimation(fig, update, frames=200, interval=200)

# 最後のアニメーションだけGIFファイルとして保存
ani.save("blockwalk.gif", writer = "pillow")
