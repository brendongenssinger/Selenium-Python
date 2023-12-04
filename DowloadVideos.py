from vimeo_downloader import Vimeo
import re


def BaixarVideos(url:str,folder:str):
    print(f'Start - > {folder}')
    CAMINHO_ORIGINAL = "D:\\VideosRodrigo\\"
    ultimo_numero = re.search(r'/(\d+)$', url).group(1)
    v = Vimeo.from_video_id(video_id=ultimo_numero)# url: https://vimeo.com/79761619
    v.best_stream.download(CAMINHO_ORIGINAL + folder)
    print(f'Finish - > {folder}')



# PRATICAS_SUTURAS_ANATOMIA_E_PARAMENTACAO = "03 - Praticas_Suturas_Anatomia e Paramentacao"
# BaixarVideos("https://player.vimeo.com/video/697514055",PRATICAS_SUTURAS_ANATOMIA_E_PARAMENTACAO)
# BaixarVideos("https://player.vimeo.com/video/697513639",PRATICAS_SUTURAS_ANATOMIA_E_PARAMENTACAO)
# BaixarVideos("https://player.vimeo.com/video/699005171",PRATICAS_SUTURAS_ANATOMIA_E_PARAMENTACAO)
# BaixarVideos("https://player.vimeo.com/video/697513274",PRATICAS_SUTURAS_ANATOMIA_E_PARAMENTACAO)
# BaixarVideos("https://player.vimeo.com/video/697513208",PRATICAS_SUTURAS_ANATOMIA_E_PARAMENTACAO)
# BaixarVideos("https://player.vimeo.com/video/697513061",PRATICAS_SUTURAS_ANATOMIA_E_PARAMENTACAO)



# DOCUMENTOS_IMPORTANTES ="04 - Documentos Importantes"
# BaixarVideos("https://player.vimeo.com/video/743748468",DOCUMENTOS_IMPORTANTES)



PRIMEIRO_MODULO ="05 - Primeiro Modulo"
BaixarVideos("https://player.vimeo.com/video/675471728",PRIMEIRO_MODULO)
BaixarVideos("https://player.vimeo.com/video/679561876",PRIMEIRO_MODULO)
BaixarVideos("https://player.vimeo.com/video/679140546",PRIMEIRO_MODULO)
BaixarVideos("https://player.vimeo.com/video/681943407",PRIMEIRO_MODULO)
BaixarVideos("https://player.vimeo.com/video/684947937",PRIMEIRO_MODULO)
BaixarVideos("https://player.vimeo.com/video/687164066",PRIMEIRO_MODULO)


Manejo_e_Tratamento_de_feridas = "06 - Manejo e Tratamento de feridas"
BaixarVideos("https://player.vimeo.com/video/690295327",Manejo_e_Tratamento_de_feridas)
BaixarVideos("https://player.vimeo.com/video/692411697",Manejo_e_Tratamento_de_feridas)



Amputacoes ="07 - Amputacoes"
BaixarVideos("https://player.vimeo.com/video/712049796",Amputacoes)
BaixarVideos("https://player.vimeo.com/video/714446190",Amputacoes)



Intensivismo = "08 - Intensivismo"
BaixarVideos("https://player.vimeo.com/video/716791408",Intensivismo)
BaixarVideos("https://player.vimeo.com/video/718716826",Intensivismo)
BaixarVideos("https://player.vimeo.com/video/724045520",Intensivismo)
BaixarVideos("https://player.vimeo.com/video/727929565",Intensivismo)
BaixarVideos("https://player.vimeo.com/video/741118708",Intensivismo)

Antimicrobianos =  "09 - Antimicrobianos"
BaixarVideos("https://player.vimeo.com/video/730330382",Antimicrobianos)
BaixarVideos("https://player.vimeo.com/video/728135515",Antimicrobianos)



Infecção_Relacionada_Assistencia_em_Saude = "10 - Infeccao_Relacionada Assistência em Saude IRAS"
BaixarVideos("https://player.vimeo.com/video/732501788",Infecção_Relacionada_Assistencia_em_Saude)
BaixarVideos("https://player.vimeo.com/video/733019933",Infecção_Relacionada_Assistencia_em_Saude)
BaixarVideos("https://player.vimeo.com/video/733023898",Infecção_Relacionada_Assistencia_em_Saude)
BaixarVideos("https://player.vimeo.com/video/733026795",Infecção_Relacionada_Assistencia_em_Saude)
BaixarVideos("https://player.vimeo.com/video/733029957",Infecção_Relacionada_Assistencia_em_Saude)
BaixarVideos("https://player.vimeo.com/video/733033042",Infecção_Relacionada_Assistencia_em_Saude)
BaixarVideos("https://player.vimeo.com/video/734733979",Infecção_Relacionada_Assistencia_em_Saude)


Pratica_De_Acesso_Abdomen = "11 - Pratica de Acesso ao Abdomen"
BaixarVideos("https://player.vimeo.com/video/717550948",Pratica_De_Acesso_Abdomen)
BaixarVideos("https://player.vimeo.com/video/717710123",Pratica_De_Acesso_Abdomen)
BaixarVideos("https://player.vimeo.com/video/717710883",Pratica_De_Acesso_Abdomen)
BaixarVideos("https://player.vimeo.com/video/717711416",Pratica_De_Acesso_Abdomen)
BaixarVideos("https://player.vimeo.com/video/717712580",Pratica_De_Acesso_Abdomen)



Pratica_De_Amputacoes = "12 - Pratica de Amputacoes"
BaixarVideos("https://player.vimeo.com/video/717715866",Pratica_De_Amputacoes)
BaixarVideos("https://player.vimeo.com/video/717717098",Pratica_De_Amputacoes)
BaixarVideos("https://player.vimeo.com/video/717716242",Pratica_De_Amputacoes)
BaixarVideos("https://player.vimeo.com/video/717720962",Pratica_De_Amputacoes)
BaixarVideos("https://player.vimeo.com/video/717722373",Pratica_De_Amputacoes)
BaixarVideos("https://player.vimeo.com/video/717723906",Pratica_De_Amputacoes)


PraticaDeCirugiasReconstrutivas = "13 - Pratica De Cirurgias Reconstrutivas"
BaixarVideos("https://player.vimeo.com/video/717727215",PraticaDeCirugiasReconstrutivas)
BaixarVideos("https://player.vimeo.com/video/717727521",PraticaDeCirugiasReconstrutivas)
BaixarVideos("https://player.vimeo.com/video/717727867",PraticaDeCirugiasReconstrutivas)
BaixarVideos("https://player.vimeo.com/video/717726898",PraticaDeCirugiasReconstrutivas)
BaixarVideos("https://player.vimeo.com/video/717726158",PraticaDeCirugiasReconstrutivas)
BaixarVideos("https://player.vimeo.com/video/717728798",PraticaDeCirugiasReconstrutivas)
BaixarVideos("https://player.vimeo.com/video/717727992",PraticaDeCirugiasReconstrutivas)
BaixarVideos("https://player.vimeo.com/video/717734535",PraticaDeCirugiasReconstrutivas)
BaixarVideos("https://player.vimeo.com/video/717735955",PraticaDeCirugiasReconstrutivas)
BaixarVideos("https://player.vimeo.com/video/717731894",PraticaDeCirugiasReconstrutivas)
BaixarVideos("https://player.vimeo.com/video/717734288",PraticaDeCirugiasReconstrutivas)
BaixarVideos("https://player.vimeo.com/video/717734028",PraticaDeCirugiasReconstrutivas)
BaixarVideos("https://player.vimeo.com/video/717737273",PraticaDeCirugiasReconstrutivas)
BaixarVideos("https://player.vimeo.com/video/717733131",PraticaDeCirugiasReconstrutivas)

Pratica_Intensivismo = "14 - Pratica de Intensivismo"
BaixarVideos("https://player.vimeo.com/video/738292007",Pratica_Intensivismo)
BaixarVideos("https://player.vimeo.com/video/738292693",Pratica_Intensivismo)
BaixarVideos("https://player.vimeo.com/video/738293835",Pratica_Intensivismo)
BaixarVideos("https://player.vimeo.com/video/738294418",Pratica_Intensivismo)
BaixarVideos("https://player.vimeo.com/video/738295467",Pratica_Intensivismo)
BaixarVideos("https://player.vimeo.com/video/738296001",Pratica_Intensivismo)
BaixarVideos("https://player.vimeo.com/video/738297391",Pratica_Intensivismo)
BaixarVideos("https://player.vimeo.com/video/740495289",Pratica_Intensivismo)
BaixarVideos("https://player.vimeo.com/video/740494876",Pratica_Intensivismo)

Hernias = "15 - Hernias "
BaixarVideos("https://player.vimeo.com/video/737670847",Hernias)
BaixarVideos("https://player.vimeo.com/video/738831252",Hernias)

CirurgiasSistemaDigestorio = "16 - Cirurgias Sistema Digestorio"
BaixarVideos("https://player.vimeo.com/video/743748699",CirurgiasSistemaDigestorio)
BaixarVideos("https://player.vimeo.com/video/746536998",CirurgiasSistemaDigestorio)
BaixarVideos("https://player.vimeo.com/video/748137587",CirurgiasSistemaDigestorio)
BaixarVideos("https://player.vimeo.com/video/750394768",CirurgiasSistemaDigestorio)
BaixarVideos("https://player.vimeo.com/video/752933161",CirurgiasSistemaDigestorio)

Urinario = "17 - Urinario"
BaixarVideos("https://player.vimeo.com/video/756465109",Urinario)
BaixarVideos("https://player.vimeo.com/video/758110892",Urinario)
BaixarVideos("https://player.vimeo.com/video/760304841",Urinario)
BaixarVideos("https://player.vimeo.com/video/762497705",Urinario)

PraticaDigestorioHernias = "18 - Praticas Digestorio e Hernias"

BaixarVideos("https://player.vimeo.com/video/758121397",PraticaDigestorioHernias)
BaixarVideos("https://player.vimeo.com/video/758122348",PraticaDigestorioHernias)
BaixarVideos("https://player.vimeo.com/video/758123813",PraticaDigestorioHernias)
BaixarVideos("https://player.vimeo.com/video/758122957",PraticaDigestorioHernias)
BaixarVideos("https://player.vimeo.com/video/758120329",PraticaDigestorioHernias)
BaixarVideos("https://player.vimeo.com/video/758128788",PraticaDigestorioHernias)
BaixarVideos("https://player.vimeo.com/video/758129763",PraticaDigestorioHernias)
BaixarVideos("https://player.vimeo.com/video/758130566",PraticaDigestorioHernias)
BaixarVideos("https://player.vimeo.com/video/758130949",PraticaDigestorioHernias)
BaixarVideos("https://player.vimeo.com/video/758131096",PraticaDigestorioHernias)
BaixarVideos("https://player.vimeo.com/video/756485211",PraticaDigestorioHernias)
BaixarVideos("https://player.vimeo.com/video/758123918",PraticaDigestorioHernias)
BaixarVideos("https://player.vimeo.com/video/758125170",PraticaDigestorioHernias)
BaixarVideos("https://player.vimeo.com/video/758127434",PraticaDigestorioHernias)
BaixarVideos("https://player.vimeo.com/video/758128273",PraticaDigestorioHernias)
BaixarVideos("https://player.vimeo.com/video/758125928",PraticaDigestorioHernias)
BaixarVideos("https://player.vimeo.com/video/758127158",PraticaDigestorioHernias)
BaixarVideos("https://player.vimeo.com/video/745108815",PraticaDigestorioHernias)

Reprodutivo = "19 - Reprodutivo"
BaixarVideos("https://player.vimeo.com/video/765074166",Reprodutivo)
BaixarVideos("https://player.vimeo.com/video/767278832",Reprodutivo)
BaixarVideos("https://player.vimeo.com/video/770897154",Reprodutivo)
BaixarVideos("https://player.vimeo.com/video/772869479",Reprodutivo)

PraticaSistemaUrinario = "20 - Pratica Sistema Urinario"
BaixarVideos("https://player.vimeo.com/video/775889783",PraticaSistemaUrinario)
BaixarVideos("https://player.vimeo.com/video/775892068",PraticaSistemaUrinario)
BaixarVideos("https://player.vimeo.com/video/775893235",PraticaSistemaUrinario)
BaixarVideos("https://player.vimeo.com/video/775895972",PraticaSistemaUrinario)
BaixarVideos("https://player.vimeo.com/video/775901096",PraticaSistemaUrinario)
BaixarVideos("https://player.vimeo.com/video/776576347",PraticaSistemaUrinario)
BaixarVideos("https://player.vimeo.com/video/776582570",PraticaSistemaUrinario)
BaixarVideos("https://player.vimeo.com/video/776612613",PraticaSistemaUrinario)

PraticaSistemaReprodutivo = "21 - Pratica Sistema Reprodutivo"

BaixarVideos("https://player.vimeo.com/video/776592954",PraticaSistemaReprodutivo)
BaixarVideos("https://player.vimeo.com/video/776588643",PraticaSistemaReprodutivo)
BaixarVideos("https://player.vimeo.com/video/776587074",PraticaSistemaReprodutivo)
BaixarVideos("https://player.vimeo.com/video/777934398",PraticaSistemaReprodutivo)
BaixarVideos("https://player.vimeo.com/video/777936122",PraticaSistemaReprodutivo)
BaixarVideos("https://player.vimeo.com/video/777934565",PraticaSistemaReprodutivo)
BaixarVideos("https://player.vimeo.com/video/777935424",PraticaSistemaReprodutivo)
BaixarVideos("https://player.vimeo.com/video/777935338",PraticaSistemaReprodutivo)
BaixarVideos("https://player.vimeo.com/video/778921837",PraticaSistemaReprodutivo)

Tcc = "22 - Tcc"
BaixarVideos("https://player.vimeo.com/video/702188999",Tcc)
BaixarVideos("https://player.vimeo.com/video/781686722",Tcc)
BaixarVideos("https://player.vimeo.com/video/843542672?share=copy",Tcc)

Oncologia = "23 - Oncologia"
BaixarVideos("https://player.vimeo.com/video/791298242",Oncologia)
BaixarVideos("https://player.vimeo.com/video/788989315",Oncologia)
BaixarVideos("https://player.vimeo.com/video/793204978",Oncologia)
BaixarVideos("https://player.vimeo.com/video/796260250",Oncologia)
BaixarVideos("https://player.vimeo.com/video/797991364",Oncologia)
BaixarVideos("https://player.vimeo.com/video/801783072",Oncologia)
BaixarVideos("https://player.vimeo.com/video/801973121",Oncologia)
BaixarVideos("https://player.vimeo.com/video/804140370",Oncologia)
BaixarVideos("https://player.vimeo.com/video/811233913",Oncologia)
BaixarVideos("https://player.vimeo.com/video/811237888",Oncologia)
BaixarVideos("https://player.vimeo.com/video/811239709",Oncologia)
BaixarVideos("https://player.vimeo.com/video/811239896",Oncologia)
BaixarVideos("https://player.vimeo.com/video/811244000",Oncologia)
BaixarVideos("https://player.vimeo.com/video/811244658",Oncologia)
BaixarVideos("https://player.vimeo.com/video/877257732?share=copy",Oncologia)


Recados2023 = "24 - Recados 2023"
BaixarVideos("https://player.vimeo.com/video/788989242",)

CirurgiasFaces = "25 - Cirurgias de Face"
BaixarVideos("https://player.vimeo.com/video/806759594",CirurgiasFaces)
BaixarVideos("https://player.vimeo.com/video/809566787",CirurgiasFaces)
BaixarVideos("https://player.vimeo.com/video/811139286",CirurgiasFaces)
BaixarVideos("https://player.vimeo.com/video/813712040",CirurgiasFaces)
BaixarVideos("https://player.vimeo.com/video/816083622",CirurgiasFaces)
BaixarVideos("https://player.vimeo.com/video/818471157",CirurgiasFaces)
BaixarVideos("https://player.vimeo.com/video/820600192?share=copy",CirurgiasFaces)
BaixarVideos("https://player.vimeo.com/video/823917610?share=copy",CirurgiasFaces)




BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)
BaixarVideos("https://player.vimeo.com/video/",)


