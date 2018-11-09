#!/usr/bin/perl
use utf8;
use CGI;
$query = new CGI;

print $query->header;
print $query->start_html('Consulta de notas CGI');
if(!$query->param) {
	print $query->start_form;
      	print $query->h3('Dime tu nombre: ');
	print $query->textfield('nombre');
	print $query->br;
      	print $query->submit(-name=>'Enviar',-value=>'Enviar');
      	print $query->end_form;
      	print $query->br;
}
else{
	if (!$query->param('nombre') eq "") {
		print $query->start_form;
     		print $query->b('Bienvenido: '),$query->param('nombre');
		print $query->br;
		print $query->h3('Dime que asignatura quieres ver: ');
		print $query->textfield('asignatura');
		print $query->submit(-name=>'enviar',-value=>'Enviar');
	      	print $query->end_form;
		print $query->br;

	}
}


if (!$query->param('enviar') eq ""){
	print $query->start_html;
      	print $query->start_form;
      	print $query->b('La asignatura elegida es '),' ', $query->param('asignatura');
	print $query->br;
	print $query->br;
	#Mirar contenido fichero notas.txt
   	open T, "/home/usuario/notas.txt";
  	while(<T>) {
  		chomp;
  		@campos=split(":");
  		if($query->param('asignatura') eq $campos[0])
  		  {
	  		print "El alumno $campos[2] tiene un $campos[1] en $campos[0]<br>";
 	  	  }
	}
	print $query->end_form;
      	print $query->br;
}
