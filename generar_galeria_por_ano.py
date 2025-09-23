import os

fotos_dir = 'Fotos'
ext_img = ('.jpg', '.jpeg', '.png', '.gif', '.jfif')
ext_vid = ('.mp4', '.mov', '.webm', '.avi', '.mkv')

for root, dirs, files in os.walk(fotos_dir):
    imagenes = [f for f in files if f.lower().endswith(ext_img)]
    videos = [f for f in files if f.lower().endswith(ext_vid)]
    if imagenes or videos:
        # Título: nombre relativo de la carpeta
        titulo = os.path.relpath(root, fotos_dir)
        if titulo == '.':
            titulo = 'Fotos'
        print(f'<p style="text-align: center; color: white; font-size: 1.5em;">{titulo}</p>')
        print('<div class="gallery">')
        for img in imagenes:
            rel_path = os.path.relpath(os.path.join(root, img), '.')
            print(f'    <img src="{rel_path}" alt="{img}">')
        for vid in videos:
            rel_path = os.path.relpath(os.path.join(root, vid), '.')
            print(f'    <video controls width="100%">')
            print(f'        <source src="{rel_path}" type="video/{os.path.splitext(vid)[1][1:]}">')
            print(f'        Tu navegador no soporta el video.')
            print(f'    </video>')
        print('</div>\n')