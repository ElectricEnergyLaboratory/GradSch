# 計算手順

今回は層状材料の電子状態を調べる目的で、Quantum ESPRESSO を使った第一原理計算を行った。構造データは Materials Project から取得したCIFファイルをベースにし、VESTA で格子定数や原子配置を確認。層間距離や周期性のチェックから、vdW相互作用が無視できない構造であることが分かった。
入力ファイルの作成には、従来の cif2qe.py は使わず、xfroggie.com のWebツールを利用。CIFをアップロードするだけで pw.x 用の入力ファイルが生成され、高対称点経路も自動抽出されるため、手作業の手間が大幅に減った。
計算条件は Quantum ESPRESSO 6.x系、擬ポテンシャルは PSLibrary の PBE を使用。vdW補正として rVV10 を加え、非局所相互作用を反映。ecutwfc = 60 Ry、ecutrho = 480 Ry を設定し、SCFでは 2×2×2、DOSでは 4×4×4 のk点メッシュを採用。バンド構造はxfroggieの経路をそのまま使った。
SCF計算後、bands.x でバンド構造を算定。DOSは dos.x で完了しており、PDOSは projwfc.x によるNSCF計算を一部実施済み。可視化は gnuplot を使わず、xfroggieの描画機能で対応した。
