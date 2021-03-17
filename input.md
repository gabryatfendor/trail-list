# Aggiungi un trail

<form action="/add-trail.py">
  <label for="lname">Nome:</label><br>
  <input type="text" id="name" name="name"><br>
  <label for="lcity">Comune:</label><br>
  <select name="city">
    <option value="Forlimpopoli" selected>Forlimpopoli</option>
    <option value="Bertinoro">Bertinoro</option>
    <option value="Faenza">Faenza</option>
    <option value="Castrocaro Terme e Terra del Sole">Castrocaro Terme e Terra del Sole</option>
    <option value="Brisighella">Brisighella</option>
  </select><br>
  <label for="ldifficulty">Difficolta':</label><br>
  <select name="difficulty">
    <option value="verde" selected>Verde</option>
    <option value="blu">Blu</option>
    <option value="rosso">Rosso</option>
    <option value="diamante nero">Diamante nero</option>
    <option value="doppio diamante nero">Doppio diamante nero</option>
  </select><br>
  <label for="ldescription">Descrizione:</label><br>
  <textarea id="description" name="description" rows="4" cols="50"></textarea><br>
  <label for="lterrain">Tipo di terreno:</label><br>
  <textarea id="terrain" name="terrain" rows="4" cols="50"></textarea><br>
  <label for="lseason">Stagione ideale':</label><br>
  <select name="season">
    <option value="non specificato" selected>Non specificato</option>
    <option value="primavera">Primavera</option>
    <option value="autunno">Autunno</option>
    <option value="inverno">Inverno</option>
    <option value="estate">Estate</option>
  </select><br>
  <label for="lgpx">Path al GPX:</label><br>
  <input type="text" id="gpx" name="gpx"><br>
  <label for="lvideo">Link al video:</label><br>
  <input type="text" id="video" name="video"><br>
  <input type="submit" value="Submit">
</form>  