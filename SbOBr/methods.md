# 計算手順

層状構造を持つ材料の電子状態を調べるため、Quantum ESPRESSO を使って第一原理計算を行った。構造情報は Materials Project から取得したCIFファイルを元にし、VESTA で格子定数や原子配置を確認した。層間距離と周期性の観察から、vdW相互作用の影響があると判断できた。
入力ファイルは cif2qe.py を使わず、xfroggie.com のツールを利用した。CIFをアップロードするだけで pw.x 用のファイルが生成され、バンド構造計算に必要な高対称点経路も自動で取得できた。手動での座標変換や経路定義が不要なのは大きな利点であると言えよう。

計算条件は以下の通りとした：Quantum ESPRESSO 6.x系、PSLibrary の PBE 擬ポテンシャル、vdW補正として rVV10 を追加した。ecutwfc = 60 Ry、ecutrho = 480 Ry を設定し、SCFでは 2×2×2、DOSでは 4×4×4 のk点メッシュを使用した。バンド構造はxfroggieが示唆する経路をそのまま使った。

SCF計算後、bands.x によるバンド構造解析を実施した。DOSは dos.x で完了させ、PDOSは projwfc.x によるNSCF計算を一部のみ実施した。可視化は xfroggie の描画機能を使い、gnuplotは使用せずに済ませた。
