syntax on
set linespace=10
set mouse=a
set sw=2
set expandtab
set smartindent
set numberwidth=1
set number
set rnu
set noswapfile
set nowrap
set nobackup
set incsearch
set clipboard=unnamedplus
set encoding=utf-8
set cursorline
set splitbelow
set splitright
set colorcolumn=128
set termguicolors

highlight ColoColumn ctermbg=0 guibg=lightgrey

source /home/aaron/.vim/Plugins.vim "fichero donde estaran los plugins

colorscheme papaya
let g:papaya_gui_color='blue'
set background=dark

"Mapeo de la barra de estado airline
let g:airline#extensions#tabline#enabled = 1  " Mostrar buffers abiertos (como pestañas)
let g:airline#extensions#tabline#fnamemod = ':t'  " Mostrar sólo el nombre del archivo
let g:airline_powerline_fonts = 1 " Modifica los separadores para que tengan forma de triangulos
let g:airline_theme='simple'

if has ('gui_runnin')
endif

"Configuracion de la indentacion 
let g:indentLine_char_list = ['│', '┊']

"configuracion de iconos
if exists("g:loaded_webdevicons")
  call webdevicons#refresh()
endif

let python_highlight_all = 1

let g:user_emmet_leader_key='<C-Z>'
