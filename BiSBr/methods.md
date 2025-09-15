# 計算手順

本研究では、層状構造を有する材料の電子状態を解析するため、Quantum ESPRESSO による第一原理計算を行った。構造データは Materials Project から取得したCIFファイルを用い、VESTA にて格子定数および原子配置を視覚的に確認した。層間距離と周期性の検討により、vdW相互作用の寄与が重要であることが示唆された。

入力ファイル作成には cif2qe.py を用いず、xfroggie.com のオンラインツールを活用した。これにより、Quantum ESPRESSO形式の入力ファイル生成に加え、高対称点経路の自動抽出が可能となり、手動設定の負担を軽減できた。

計算には Quantum ESPRESSO 6.x系 を使用し、PSLibrary の PBE 擬ポテンシャルを選定。交換相関汎関数には rVV10 によるvdW補正を加えた。ecutwfc = 60 Ry、ecutrho = 480 Ry の条件下でSCF計算を行い、k点は 2×2×2（SCF）、4×4×4（DOS）とした。バンド構造はxfroggieの経路をそのまま利用した。

SCF計算後、bands.x によるバンド構造解析を実施。DOSは dos.x にて算定済みであり、PDOSは projwfc.x によるNSCF計算を一部実施した段階である。可視化には gnuplot を用いず、xfroggieの描画機能を利用した。
