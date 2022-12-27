$("#select").change(function () {
  var value = $("#select option:selected").text();
  var largura = document.getElementById("largura");
  var perfil = document.getElementById("perfil");
  var tamanho = document.getElementById("tamanho");
  // var marca = document.getElementById("marca");
  var tipo = document.getElementById("tipo");
  var material = document.getElementById("material");
  var cor = document.getElementById("cor");
  var btn = document.getElementById("btn");
  var quant = document.getElementById("quant");
  var img = document.getElementById("img");
  var valor = document.getElementById("valor");

  console.log(value);
  $(largura).hide();
  $(tipo).hide();
  $(perfil).hide();
  $(tamanho).hide();
  $(material).hide();
  $(cor).hide();
  $(btn).hide();
  $(quant).hide();
  $(valor).hide();
  $(img).hide();
  

  if (value.toLowerCase() === "pneu") {
    console.log("Mizera dos inferno");
    $(largura).show();
    $(perfil).show();
    $(tamanho).show();
    $(btn).show();
    $(quant).show();
    $(valor).show();
    $(img).show();
  }

  if (value.toLowerCase() === "aro") {
    $(largura).show();
    $(perfil).show();
    $(tamanho).show();
    $(material).show();
    $(cor).show();
    $(btn).show();
    $(quant).show();
    $(valor).show();
    $(img).show();
  }

  if (value.toLowerCase() === "raio") {
    $(largura).show();
    $(perfil).show();
    $(tamanho).show();
    $(tipo).show();
    $(material).show();
    $(cor).show();
    $(btn).show();
    $(quant).show();
    $(valor).show();
    $(img).show();
  }

  if (value.toLowerCase() === "farol") {
    $(tamanho).show();
    $(tipo).show();
    $(material).hide();
    $(btn).show();
    $(quant).show();
    $(valor).show();
    $(img).show();
  }
  if (value.toLowerCase() === "retrovisor") {
    $(tamanho).show();
    $(tipo).show();
    $(material).show();
    $(cor).show();
    $(btn).show();
    $(quant).show();
    $(valor).show();
    $(img).show();
  }
});
