const canvas = document.getElementById('logoCanvas');
const ctx = canvas.getContext('2d');

const text = 'Black Stack Hub';
const textSize = Math.min(window.innerWidth, window.innerHeight) * 0.1;
ctx.font = `bold ${textSize}px Arial`;
const textWidth = ctx.measureText(text).width;
const textHeight = textSize*1.8;
canvas.width = window.innerWidth;
canvas.height = window.innerHeight-(window.innerHeight/5);

let particlesArray = [];
const mouse = {
    x: null,
    y: null,
    radius: 30
};

window.addEventListener('mousemove', function(event) {
    mouse.x = event.x - canvas.getBoundingClientRect().left;
    mouse.y = event.y - canvas.getBoundingClientRect().top;
});

ctx.fillStyle = 'white';
ctx.font = `bold ${textSize}px Arial`;
ctx.fillText(text, 0, textSize - 5);
ctx.textAlign = 'center';
ctx.textBaseline = 'middle';

const textCoordinates = ctx.getImageData(0, 0, textWidth, textSize);

class Particle {
    constructor(x, y) {
        this.baseX = x;
        this.baseY = y;
        this.x = x;
        this.y = y;
        this.size = 1.5;
        this.density = (Math.random() * 30) + 1;
        this.color = 'white';
        this.randomAnimationStartTime = Math.random() * 3000;
        this.isAnimated = Math.random() > 0.9;
    }

    draw() {
        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.closePath();
        ctx.fill();
    }

    update() {
        let dx = mouse.x - this.x;
        let dy = mouse.y - this.y;
        let distance = Math.sqrt(dx * dx + dy * dy);
        let forceDirectionX = dx / distance;
        let forceDirectionY = dy / distance;
        let maxDistance = mouse.radius;
        let force = (maxDistance - distance) / maxDistance;
        let directionX = forceDirectionX * force * this.density;
        let directionY = forceDirectionY * force * this.density;

        if (distance < mouse.radius) {
            this.x -= directionX * 10;
            this.y -= directionY * 10;
        } else {
            if (this.x !== this.baseX) {
                let dx = this.x - this.baseX;
                this.x -= dx / 10;
            }
            if (this.y !== this.baseY) {
                let dy = this.y - this.baseY;
                this.y -= dy / 10;
            }
        }

        if (this.isAnimated) {
            let currentTime = new Date().getTime();
            let animationDuration = 100;
            if (currentTime - this.randomAnimationStartTime > animationDuration) {
                this.randomAnimationStartTime = currentTime + Math.random() * 3000;
                this.color = this.color === 'white' ? 'black' : 'white';
            }
        }
    }
}

function init() {
    particlesArray = [];
    for (let y = 0, y2 = textCoordinates.height; y < y2; y+=3) {
        for (let x = 0, x2 = textCoordinates.width; x < x2; x+=3) {
            if (textCoordinates.data[(y * 4 * textCoordinates.width) + (x * 4) + 3] > 128) {
                let positionX = x+(canvas.width - textWidth) / 2;
                let positionY = y+(canvas.height - (textHeight/2)) / 2;
                particlesArray.push(new Particle(positionX, positionY));
            }
        }
    }
}

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let i = 0; i < particlesArray.length; i++) {
        particlesArray[i].draw();
        particlesArray[i].update();
    }
    requestAnimationFrame(animate);
}

init();
animate();

window.onresize = function() {
    window.location.reload();
};

document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('.section');

    links.forEach(link => {
      link.addEventListener('click', function(event) {
        event.preventDefault();
        const targetId = this.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);
        
        if (targetElement) {
            sections.forEach(container => {
            container.classList.remove('active');
          });

          targetElement.classList.add('active');
        }
      });
    });
});

