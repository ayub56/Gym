<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Star Gym</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap');

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Poppins', sans-serif;
    }

    body {
      background: #121212;
      color: #eee;
      line-height: 1.6;
    }
    header {
      background: linear-gradient(90deg, #ff416c, #ff4b2b);
      padding: 2rem 1rem;
      text-align: center;
      position: sticky;
      top: 0;
      z-index: 1000;
      box-shadow: 0 2px 10px rgba(255, 75, 43, 0.5);
    }

    header h1 {
      font-size: 2.5rem;
      font-weight: 600;
    }

    nav {
      margin-top: 0.75rem;
    }

    nav a {
      color: #ffe;
      text-decoration: none;
      margin: 0 1rem;
      font-weight: 600;
      transition: color 0.3s ease;
    }

    nav a:hover {
      color: #ffd700;
    }

    .hero {
      background: url('https://images.unsplash.com/photo-1554284126-7e45ae576c75?auto=format&fit=crop&w=1470&q=80') no-repeat center center/cover;
      height: 90vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      padding: 0 1rem;
      color: white;
      text-shadow: 0 0 15px rgba(0, 0, 0, 0.7);
    }

    .hero h2 {
      font-size: 3rem;
      font-weight: 700;
      margin-bottom: 1rem;
      letter-spacing: 2px;
      text-transform: uppercase;
    }

    .hero p {
      max-width: 600px;
      font-size: 1.25rem;
      margin-bottom: 2rem;
      font-weight: 300;
    }

    .btn-hero {
      background: #ff416c;
      color: white;
      padding: 0.75rem 2rem;
      border: none;
      border-radius: 35px;
      font-weight: 600;
      font-size: 1.1rem;
      cursor: pointer;
      transition: background 0.3s ease;
      box-shadow: 0 4px 15px #ff416c;
      user-select: none;
    }

    .btn-hero:hover {
      background: #ff4b2b;
      box-shadow: 0 6px 20px #ff4b2b;
    }

    section {
      max-width: 1100px;
      margin: 4rem auto;
      padding: 0 1rem;
    }

    h3.section-title {
      text-align: center;
      font-size: 2.25rem;
      margin-bottom: 2rem;
      font-weight: 600;
      color: #ff416c;
      text-transform: uppercase;
      letter-spacing: 3px;
    }

    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.5rem;
    }

    .card {
      background: #1f1f1f;
      border-radius: 15px;
      overflow: hidden;
      box-shadow: 0 8px 20px rgba(255, 75, 43, 0.3);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      height: 100%;
    }

    .card:hover {
      transform: translateY(-10px);
      box-shadow: 0 14px 30px rgba(255, 75, 43, 0.6);
    }

    .card img {
      width: 100%;
      height: 180px;
      object-fit: cover;
      aspect-ratio: 4 / 3;
    }

    .card-content {
      padding: 1rem 1.5rem;
      flex-grow: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .card-content h4 {
      color: #ff4b2b;
      font-weight: 700;
      margin-bottom: 0.75rem;
      font-size: 1.3rem;
    }

    .card-content p {
      font-weight: 300;
      flex-grow: 1;
      margin-bottom: 1rem;
      color: #ddd;
    }

    .deal-price {
      font-size: 1.5rem;
      font-weight: 700;
      color: #ffd700;
      margin-bottom: 1rem;
    }

    .card-content button {
      background: #ff416c;
      color: white;
      border: none;
      padding: 0.5rem 1.5rem;
      border-radius: 35px;
      font-weight: 600;
      transition: background 0.3s ease;
      cursor: pointer;
      align-self: flex-start;
      box-shadow: 0 4px 10px #ff416c;
    }

    .card-content button:hover {
      background: #ff4b2b;
      box-shadow: 0 6px 15px #ff4b2b;
    }

    footer {
      background: #181818;
      text-align: center;
      padding: 2rem 1rem;
      color: #666;
      font-weight: 300;
      font-size: 0.9rem;
      border-top: 1px solid #333;
    }

    /* Responsive Text Scaling */
    @media (max-width: 600px) {
      .hero h2 {
        font-size: 2rem;
      }

      .hero p {
        font-size: 1rem;
      }

      header h1 {
        font-size: 1.75rem;
      }

      h3.section-title {
        font-size: 1.8rem;
      }
    }
  </style>
</head>
<body>
  <header>
    <h1>Star Gym</h1>
    <nav>
      <a href="#deals">Deals</a>
      <a href="#offers">Offers</a>
      <a href="#sales">Sales</a>
      <a href="#exciting">Membership</a>
    </nav>
  </header>

  <section class="hero" aria-label="Gym introduction and hero image">
    <h2>Unleash Your Power</h2>
    <p>Join PowerFit Gym today and transform your body & mind with the best training experience.</p>
    <button class="btn-hero" onclick="scrollToSection('deals')">Check Our Deals</button>
  </section>

  <section id="deals" aria-label="Gym Deals Section">
    <h3 class="section-title">Amazing Deals</h3>
    <div class="cards">
      <article class="card">
        <img src="https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=600&q=80" alt="Personal trainer guiding a gym member"/>
        <div class="card-content">
          <h4>Personal Training</h4>
          <p>Get 30% off on personal training packages for 3 months.</p>
          <div class="deal-price">$199 <small>/ 3 months</small></div>
          <button>Sign Up</button>
        </div>
      </article>
      <article class="card">
        <img src="gym 1.jpg" alt="Group fitness class exercising together"/>
        <div class="card-content">
          <h4>Group Classes</h4>
          <p>Unlimited access to all group classes. Limited time 25% discount!</p>
          <div class="deal-price">$75 <small>/ month</small></div>
          <button>Join Now</button>
        </div>
      </article>
      <article class="card">
        <img src="member.jpg" alt="Gym memberships card"/>
        <div class="card-content">
          <h4>Annual Membership</h4>
          <p>Pay for 10 months, enjoy the full year! 2 months free with annual membership.</p>
          <div class="deal-price">$500 <small>/ year</small></div>
          <button>Become Member</button>
        </div>
      </article>
    </div>
  </section>

  <section id="offers" aria-label="Special Offers Section">
    <h3 class="section-title">Special Offers</h3>
    <div class="cards">
      <article class="card">
        <img src="diet.webp" alt="Healthy meal preparation"/>
        <div class="card-content">
          <h4>Nutrition Plan</h4>
          <p>Get a free personalized nutrition plan with your membership this month!</p>
          <button>Learn More</button>
        </div>
      </article>
      <article class="card">
        <img src="yoga" alt="Yoga session in the gym"/>
        <div class="card-content">
          <h4>Yoga Workshops</h4>
          <p>Experience peace of mind with our free yoga workshops every weekend.</p>
          <button>Reserve Spot</button>
        </div>
      </article>
      <article class="card">
        <img src="inside.jpg" alt="Gym with state of the art equipment"/>
        <div class="card-content">
          <h4>New Equipment Launch</h4>
          <p>Try out state-of-the-art machines with exclusive introductory sessions.</p>
          <button>Book Trial</button>
        </div>
      </article>
    </div>
  </section>

  <section id="sales" aria-label="Gym Sales Section">
    <h3 class="section-title">Hot Sales</h3>
    <div class="cards">
      <article class="card">
        <img src="merchant.jpg" alt="Gym apparel and merchandise"/>
        <div class="card-content">
          <h4>Merchandise Discount</h4>
          <p>Get 40% off on all PowerFit branded apparel and accessories this weekend only!</p>
          <button>Shop Now</button>
        </div>
      </article>
      <article class="card">
        <img src="supplement.jpg" alt="Gym supplement products"/>
        <div class="card-content">
          <h4>Supplement Sale</h4>
          <p>Buy 2 get 1 free on all protein powders and supplements.</p>
          <button>Order Now</button>
        </div>
      </article>
      <article class="card">
        <img src="gear.jpg" alt="Workout gear and shoes"/>
        <div class="card-content">
          <h4>Gear Clearance</h4>
          <p>Up to 50% off on select workout gear. Perfect time to upgrade your kit!</p>
          <button>Buy Now</button>
        </div>
      </article>
    </div>
  </section>

  <section id="exciting" aria-label="Exciting Things Section">
    <h3 class="section-title">Exciting Things</h3>
    <div class="cards">
      <article class="card">
        <img src="https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=600&q=80" alt="Virtual Reality Fitness Experience"/>
        <div class="card-content">
          <h4>VR Fitness Experience</h4>
          <p>Step into the future with our new Virtual Reality workout sessions – immersive and fun!</p>
          <button>Try VR</button>
        </div>
      </article>
      <article class="card">
        <img src="challange.jpg" alt="Fitness challenge competition"/>
        <div class="card-content">
          <h4>Monthly Challenges</h4>
          <p>Compete with gym members, win prizes, and push your limits every month!</p>
          <button>Join Challenge</button>
        </div>
      </article>
      <article class="card">
        <img src="app.png" alt="PowerFit mobile app on phone"/>
        <div class="card-content">
          <h4>PowerFit App</h4>
          <p>Monitor your progress, book classes and track your goals with our new app.</p>
          <button>Download Now</button>
        </div>
      </article>
    </div>
  </section>

  <footer>
    &copy; 2024 Star Gym — Feel the Power, Be the Power.
  </footer>

  <script>
    function scrollToSection(id) {
      const el = document.getElementById(id);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }
  </script>
  <script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>
<df-messenger
  intent="WELCOME"
  chat-title="Gym"
  agent-id="efd5c898-2852-46ac-8dfa-4921a8678c56"
  language-code="en"
></df-messenger>
</body>
</html>

