const sections = document.querySelectorAll("section");

window.addEventListener("scroll", () => {
  sections.forEach(section => {
    const top = section.getBoundingClientRect().top;
    if (top < window.innerHeight - 100) {
      section.classList.add("show");
    }
  });
});


if (document.getElementById("particles-bg")) {
  tsParticles.load("particles-bg", {
    fullScreen: false,
    background: {
      color: "transparent"
    },
    particles: {
      number: {
        value: 18,
        density: {
          enable: true,
          area: 800
        }
      },
      color: {
        value: ["#38bdf8", "#818cf8", "#f472b6"]
      },
      shape: {
        type: "circle"
      },
      opacity: {
        value: 0.35
      },
      size: {
        value: {min: 80, max: 160}
      },
      move: {
        enable: true,
        speed: 0.6,
        direction: "none",
        random: true,
        straight: false,
        outModes: {
          default: "out"
        }
      }
    },
    interactivity: {
      events: {
        onHover: {
          enable: true,
          mode: "repulse"
        }
      },
      modes: {
        repulse: {
          distance: 120,
          duration: 0.4
        }
      }
    },
    detectRetina: true
  });

}


  const form = document.getElementById("contactForm");

  form.addEventListener("submit", function(e) {
  const formData = {
  name: form.name.value,
  email: form.email.value,
  message: form.message.value
};
  sessionStorage.setItem("pendingFormData", JSON.stringify(formData));
});





document.addEventListener("DOMContentLoaded", function() {
  var typed = new Typed("#typed-text", {
    strings: ["Welcome to my Portfolio"],
    typeSpeed: 100,   // speed of typing in milliseconds
    backSpeed: 0,     // no backspace
    loop: false       // type only once
  });
});






