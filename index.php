<DOCTYPE html>
<html>
    <head>
        <title>tecblog</title>
        <link rel="stylesheet" type="text/css" href="./css/estilos.css">
    </head>
    <body>
        <form name="principal" method="post" action="">
            <table width="1400px" cellpadding="0px" cellspacing="0px" border="0">
                <?php 
                    require_once("./pages/titulo.php");
                    require_once("./pages/menu.php");
                    if(isset($_REQUEST["opcao"])) 
                    {
                        if($_REQUEST["opcao"] ==""){
                            require_once("./pages/home.php");
                        }
                        else if($_REQUEST["opcao"] == "home"){
                            require_once("./pages/home.php");
                        }
                        else if($_REQUEST["opcao"] == "jogos"){
                            require_once("./pages/jogos.php");
                        }
                        else if($_REQUEST["opcao"] == "celulares"){
                            require_once("./pages/celulares.php");
                        }
                        else if($_REQUEST["opcao"] == "computadores"){
                            require_once("./pages/computadores.php");
                        }
                        else if($_REQUEST["opcao"] == "contato"){
                            require_once("./pages/contato.php");
                        }
                        else if($_REQUEST["opcao"] == "cadastrese"){
                            require_once("./pages/cadastrese.php");
                        }
                        else{
                            require_once("./pages/home.php");
                        }
                    }
                    
                    require_once("./pages/rodape.php");
                ?>
            </table>
        </form>
    </body>
</html>