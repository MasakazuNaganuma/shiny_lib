# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 23:14:05 2024

@author: mnaganuma
"""

def std_input(file_path):
    """
    指定されたファイルを読み込んでその内容を返す関数。

    Parameters:
    - file_path (str): 読み込むファイルのパス。

    Returns:
    - str or None: ファイルの内容（文字列）を返す。ファイルが見つからない場合や読み込み中にエラーが発生した場合はNoneを返す。

    Raises:
    - FileNotFoundError: 指定されたパスのファイルが見つからない場合に発生。
    - Exception: その他の読み込み中のエラーが発生した場合に発生。

    Example:
    >>> file_path = "sample.txt"
    >>> content = std_input(file_path)
    >>> if content:
    >>>     print(content)
    >>> else:
    >>>     print(f"ファイル '{file_path}' を読み込めませんでした。")
    """
    try:
        # ファイルを開く
        with open(file_path, 'r', encoding='utf-8') as file:
            # ファイルの内容を読み込む
            content = file.read()
            content_list = content.splitlines()
            return content_list
    
    except FileNotFoundError:
        print(f"ファイル '{file_path}' が見つかりませんでした。")
    
    except Exception as e:
        print(f"ファイルの読み込み中にエラーが発生しました: {e}")
