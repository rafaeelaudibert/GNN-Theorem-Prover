# Changer cette ligne pour votre site favori
WWWDIR = /www/html/DN
# Le répertoire ci-dessus doit être sur la même machine que celle de la
# compilation, sous peine d'avoir des problèmes
# Le source du site doit être placé à la racine du site

WWWFILES = index.php \
	syntax.php \
	download.php \
	rules.php \
	examples.php \
	info.php \
	header.inc \
	footer.inc \
	safeassistant 

CAMLC=ocamlc
CAMLYACC=ocamlyacc
CAMLLEX=ocamllex



assistant :  lexer.cmo parser.cmo interface.cmo  preuve.cmo  assistant.cmo 
	$(CAMLC) -o assistant lexer.cmo parser.cmo interface.cmo preuve.cmo   assistant.cmo

assistant.cmo : assistant.ml 	preuve.cmo  interface.cmo lexer.cmo parser.cmo parser.cmi 
	$(CAMLC) -c assistant.ml



preuve.cmo : preuve.ml    interface.cmo lexer.cmo parser.cmo  
	$(CAMLC) -c preuve.ml


lexer.ml: lexer.mll parser.cmo
	$(CAMLLEX) lexer.mll

parser.mli parser.ml: parser.mly interface.cmo
	$(CAMLYACC) parser.mly

lexer.cmo: parser.cmi

parser.cmi: parser.mli
	$(CAMLC) -c parser.mli


interface.cmo : interface.ml
	$(CAMLC) -c interface.ml

lexer.cmo : lexer.ml
	$(CAMLC) -c lexer.ml

parser.cmo: parser.ml parser.cmi
	$(CAMLC) -c parser.ml


www :   assistant $(WWWFILES)
	cp assistant $(WWWFILES) $(WWWDIR)
	chmod a+rx $(WWWDIR)/*

clean:
	rm -f lexer.ml parser.ml parser.mli *.cmi *.cmo 



