$(document).ready(function() {
  $("#btn").click(function() {
    // Obter os valores dos inputs
    var data = $("#data").val();
    var cGrandes = $("#cgrandes").val();
    var cPequenos = $("#cpequenos").val();

    // Fazer a requisição para o backend
    $.ajax({
      url: "http://localhost:5000/api/CalcularMelhorPetshop",
      type: "POST",
      data: JSON.stringify({
        Data: data,
        CaesPequenos: cPequenos,
        CaesGrandes: cGrandes,
      }),
      success: function(result) {
        // Atualizar a página com os resultados
        $("#petshop-nome").text(result.NomePetshop);
        $("#petshop-valor").text("R$ " + result.PrecoTotal.toFixed(2));
        $("#petshop-dist").text(result.Distancia + " km");
        $("#petshop-dia").text(data);
        $("#sidebar").hide(); // Esconde a barra lateral na hora de mostrar ls resultados
        $("#inputs").hide();
        $("#outputs").show();
      },
      error: function(error) {
        console.error("Erro ao calcular o melhor petshop:", error);
      },
    });
  });

  $("#ret").click(function() {
    // Reiniciar a pesquisa
    $("#inputs").show();
    $("#outputs").hide();
    $("#sidebar").show();
  });
});