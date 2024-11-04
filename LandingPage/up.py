import sqlite3
from sqlite3 import Error

# Establish a connection to your SQLite database
try:
    connection = sqlite3.connect('tech_reviews.db')  # SQLite uses a single file for the database

    cursor = connection.cursor()

    # Create the "TechReviews" table if it doesn't exist
    create_table_query = '''CREATE TABLE IF NOT EXISTS TechReviews (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                image BLOB NOT NULL,
                                description TEXT NOT NULL
                            );'''
    cursor.execute(create_table_query)

    img_paths = [
        "./img/1.jpg", "./img/2.jpg", "./img/3.jpg", "./img/4.jpg", "./img/5.jpg",
        "./img/6.jpg", "./img/7.jpg", "./img/8.jpg", "./img/9.jpg", "./img/10.jpg",
        "./img/11.jpg", "./img/12.jpg", "./img/13.jpg", "./img/14.jpg", "./img/15.jpg",
        "./img/16.jpg", "./img/17.jpg", "./img/18.jpg", "./img/19.jpg", "./img/20.jpg",
        "./img/21.jpg", "./img/22.jpg", "./img/23.jpg", "./img/24.jpg", "./img/25.jpg",
        "./img/26.jpg", "./img/27.jpg", "./img/28.jpg", "./img/29.jpg", "./img/30.jpg",
        "./img/31.jpg", "./img/32.jpg", "./img/33.jpg", "./img/34.jpg", "./img/35.jpg",
        "./img/36.jpg", "./img/37.jpg", "./img/38.jpg", "./img/39.jpg", "./img/40.jpg",
        "./img/41.jpg", "./img/42.jpg", "./img/43.jpg", "./img/44.jpg", "./img/45.jpg",
        "./img/46.jpg", "./img/47.jpg", "./img/48.jpg", "./img/49.jpg", "./img/50.jpg"
    ]

    file = [
        (1, "Python", "Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python's design emphasizes code readability with its use of significant indentation. It comes with a comprehensive standard library and is widely used in web development, data analysis, artificial intelligence, and scientific computing. Python is praised for its strong community support and versatile frameworks like Django and Flask."),

        (2, "JavaScript", "JavaScript is a versatile, high-level programming language used for creating interactive web content. It is integral to modern web development, working alongside HTML and CSS. JavaScript enables dynamic user interfaces, event handling, and asynchronous operations. It runs in browsers and on servers with Node.js. Modern frameworks like React, Angular, and Vue.js have enhanced its capabilities for building complex web applications, making it a cornerstone of front-end development."),

        (3, "Java", "Java is a widely-used, object-oriented programming language known for its principle of 'write once, run anywhere.' It achieves this through the Java Virtual Machine (JVM), which allows applications to run on any device with a JVM. Java simplifies many complexities of C++ and is extensively used in enterprise environments, Android development, and large-scale web applications. Its robust libraries and frameworks, like Spring and Hibernate, contribute to its widespread use."),
 
        (4, "C++", "C++ is an extension of the C programming language with added object-oriented features. It is renowned for its performance and efficiency, making it suitable for system/software development, game development, and applications requiring high-performance graphics. C++ allows for low-level data and memory manipulation, offering developers control over system resources. Despite its complexity, it remains a powerful tool for performance-critical applications."),
 
        (5, "HTML", "HTML (HyperText Markup Language) is the standard markup language used to structure web content. It defines elements and tags for creating headings, paragraphs, links, images, and other content on web pages. HTML forms the foundation of web development, working with CSS and JavaScript to enhance the appearance and functionality of web content. HTML5 introduces new elements and APIs that support multimedia, animations, and local storage, advancing web capabilities."),

        (6, "CSS", "CSS (Cascading Style Sheets) is a stylesheet language used to describe the presentation of web pages. It allows developers to separate content from design, controlling aspects like colors, fonts, spacing, and layout. CSS3 introduces features such as media queries for responsive design, transitions, and animations. CSS enhances the visual appeal and adaptability of web pages across different devices and screen sizes, making it an essential tool for modern web design."),
 
        (7, "SQL", "SQL (Structured Query Language) is a domain-specific language for managing and manipulating relational databases. It provides a standardized way to query data, insert records, update information, and delete entries. SQL is crucial for interacting with relational database management systems (RDBMS) such as MySQL, PostgreSQL, and Oracle. It supports defining and managing database schemas, creating relationships between tables, and ensuring data integrity."),
 
        (8, "Ruby", "Ruby is a dynamic, open-source programming language focused on simplicity and productivity. It features an elegant syntax designed to be easy to read and write. Ruby supports multiple programming paradigms, including object-oriented and functional programming. It is best known for the Ruby on Rails framework, which simplifies web development with conventions and built-in tools, promoting developer happiness and efficient application creation."),
 
        (9, "PHP", "PHP (Hypertext Preprocessor) is a widely-used scripting language for server-side web development. It can be embedded within HTML to generate dynamic web content. PHP integrates well with databases like MySQL and PostgreSQL and supports various web technologies and frameworks, including Laravel and Symfony. Its ease of use and flexibility have made it a popular choice for creating scalable and maintainable web applications."),
 
        (10, "Swift", "Swift is a programming language developed by Apple for building applications across its ecosystem, including iOS, macOS, watchOS, and tvOS. It is designed to be both expressive and efficient, with features that enhance code readability and maintainability. Swift offers strong type inference, memory safety, and error handling capabilities. Its modern syntax, combined with advanced features like optionals and protocols, makes it a powerful tool for creating high-performance applications on Apple platforms."),
 
        (11, "TypeScript", "TypeScript is a superset of JavaScript that adds static typing to the language. Developed by Microsoft, it aims to improve the development process by catching errors at compile time rather than runtime. TypeScript offers features like interfaces, generics, and modules that help in building large-scale applications. It is widely used in conjunction with modern JavaScript frameworks such as Angular and React, providing enhanced tooling and better code quality."),
 
        (12, "Go", "Go, also known as Golang, is a statically typed, compiled programming language designed by Google. It is known for its simplicity, performance, and strong concurrency support. Go features a garbage collector and a built-in concurrency model called goroutines, making it suitable for building scalable and high-performance applications. It is often used for backend services, cloud computing, and distributed systems."),
 
        (13, "Kotlin", "Kotlin is a modern, statically typed programming language developed by JetBrains. It is designed to be fully interoperable with Java while addressing some of its shortcomings. Kotlin provides features like null safety, extension functions, and data classes, making it a more expressive and safer language for Android development. It is officially supported by Google for Android development and has been gaining popularity for server-side applications."),
 
        (14, "Rust", "Rust is a systems programming language focused on safety and performance. It aims to prevent memory errors such as null pointer dereferencing and buffer overflows through its ownership system and strong type checking. Rust provides fine-grained control over system resources while maintaining high performance. It is increasingly used in systems programming, web assembly, and other performance-critical applications."),
 
        (15, "Perl", "Perl is a high-level, general-purpose programming language known for its text-processing capabilities. It is often used in system administration, web development, and network programming. Perl's syntax is highly flexible, allowing developers to write concise and powerful scripts. It has a rich ecosystem of modules and libraries, making it suitable for a wide range of tasks, from CGI scripting to complex data analysis."),
 
        (16, "Dart", "Dart is a client-optimized programming language developed by Google for building modern web and mobile applications. It is the language behind the Flutter framework, which allows for cross-platform app development. Dart features a strong static type system and asynchronous programming support, providing a productive environment for building high-performance applications with smooth user experiences."),
 
        (17, "MATLAB", "MATLAB is a high-level programming language and environment used for numerical computing, data analysis, and visualization. It is widely used in academia and industry for tasks such as algorithm development, data analysis, and simulation. MATLAB offers built-in functions and toolboxes for various applications, including signal processing, image processing, and machine learning, making it a powerful tool for engineering and scientific research."),
 
        (18, "R", "R is a programming language and software environment specifically designed for statistical computing and data analysis. It provides a wide range of statistical and graphical techniques and is highly extensible through packages. R is widely used in data science, bioinformatics, and social sciences for data manipulation, visualization, and statistical modeling. Its active community continuously contributes to its extensive ecosystem."),
 
        (19, "Scala", "Scala is a hybrid programming language that combines object-oriented and functional programming paradigms. It runs on the Java Virtual Machine (JVM) and is interoperable with Java, allowing developers to use Java libraries and frameworks. Scala's concise syntax, powerful type system, and support for higher-order functions make it a popular choice for complex data processing, distributed computing, and concurrent programming."),
 
        (20, "Haskell", "Haskell is a purely functional programming language known for its strong static type system and lazy evaluation. It emphasizes immutability and higher-order functions, making it well-suited for mathematical and algorithmic applications. Haskell's type system helps catch errors at compile time, and its advanced features like monads and type inference enable developers to write concise and robust code."),
 
        (21, "Erlang", "Erlang is a programming language designed for concurrent and distributed systems. It features lightweight processes, message passing, and fault tolerance, making it suitable for building reliable and scalable applications. Erlang is used in telecommunications, messaging systems, and real-time applications. Its runtime system supports hot code swapping, allowing for updates without stopping the system."),
 
        (22, "Lua", "Lua is a lightweight, embeddable scripting language known for its simplicity and flexibility. It is often used as an embedded language in applications, game development, and configuration files. Lua's minimalistic design and fast execution make it suitable for use in resource-constrained environments. It provides easy integration with C and C++ and supports procedural, object-oriented, and functional programming styles."),
 
        (23, "C#", "C# is a modern, object-oriented programming language developed by Microsoft as part of the .NET framework. It is designed for building a wide range of applications, from web services to desktop applications and games. C# combines features from C++ and Java, offering strong type safety, garbage collection, and language interoperability. It is widely used for Windows application development and in game development with Unity."),
 
        (24, "PowerShell", "PowerShell is a task automation and configuration management framework developed by Microsoft. It includes a command-line shell and scripting language that allows administrators to manage and automate system tasks. PowerShell provides access to .NET objects and supports complex scripting with features like pipelines, cmdlets, and remote management. It is commonly used for system administration and automation in Windows environments."),
 
        (25, "Shell Scripting", "Shell scripting involves writing scripts for command-line interfaces to automate tasks in Unix-like operating systems. Shell scripts use shell commands and programming constructs to perform tasks such as file manipulation, program execution, and system monitoring. Popular shells for scripting include Bash, Zsh, and Fish. Shell scripting is essential for system administration, automation, and workflow optimization."),
 
        (26, "HTML5", "HTML5 is the latest version of the HyperText Markup Language used to structure and present web content. It introduces new elements and APIs for creating rich, interactive web applications. Features like the `<canvas>` element for graphics, the `<video>` and `<audio>` elements for multimedia, and local storage support enable developers to build modern, multimedia-rich websites and applications."),
 
        (27, "GraphQL", "GraphQL is a query language for APIs and a runtime for executing queries by providing a more efficient and flexible alternative to REST. It allows clients to request specific data and receive exactly what they need, reducing over-fetching and under-fetching issues. GraphQL provides a single endpoint for all interactions and supports real-time updates through subscriptions, making it a popular choice for modern API design."),
 
        (28, "RESTful APIs", "RESTful APIs (Representational State Transfer) are a set of architectural principles for designing networked applications. They use HTTP requests to perform CRUD (Create, Read, Update, Delete) operations on resources represented in a stateless manner. RESTful APIs are widely used for web services due to their simplicity, scalability, and ease of integration with web technologies. They rely on standard HTTP methods like GET, POST, PUT, and DELETE."),

        (29, "WebAssembly", "WebAssembly (Wasm) is a binary instruction format for a stack-based virtual machine, designed to enable high-performance execution of code on web browsers. It allows developers to run code written in languages like C, C++, and Rust on the web with near-native speed. WebAssembly complements JavaScript by providing a low-level, efficient compilation target, enhancing performance for computationally intensive tasks and applications."),

        (30, "Docker", "Docker is an open-source platform that automates the deployment of applications inside lightweight, portable containers. Containers encapsulate an application and its dependencies, ensuring consistency across different environments. Docker simplifies the development, testing, and deployment processes, making it easier to manage and scale applications. It is widely used for microservices architecture, continuous integration, and DevOps practices."),
 
        (31, "Kubernetes", "Kubernetes is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications. It provides features like load balancing, service discovery, and automated rollouts and rollbacks. Kubernetes helps manage complex containerized applications across clusters of machines, ensuring high availability and scalability. It is a key technology for modern cloud-native application deployment."),
 
        (32, "Apache Kafka", "Apache Kafka is a distributed streaming platform used for building real-time data pipelines and streaming applications. It is designed to handle high-throughput, fault-tolerant messaging between distributed systems. Kafka provides features like publish-subscribe messaging, stream processing, and data storage. It is commonly used for event-driven architectures, log aggregation, and real-time analytics."),
 
        (33, "Redis", "Redis is an open-source, in-memory data structure store used as a database, cache, and message broker. It supports various data types such as strings, hashes, lists, sets, and sorted sets. Redis is known for its high performance and low latency, making it suitable for real-time applications. It provides features like persistence, replication, and high availability, and is often used for caching, session storage, and message queuing."),

        (34, "Elasticsearch", "Elasticsearch is a distributed search and analytics engine built on top of Apache Lucene. It provides full-text search capabilities, real-time indexing, and analytics for large volumes of data. Elasticsearch is often used for log and event data analysis, application search, and enterprise search solutions. It is part of the Elastic Stack, which includes Kibana for visualization and Logstash for data processing."),

        (35, "Terraform", "Terraform is an open-source infrastructure as code (IaC) tool developed by HashiCorp. It allows users to define and provision infrastructure using a declarative configuration language. Terraform supports multiple cloud providers and on-premises infrastructure, enabling automated and consistent management of resources. It provides features like resource dependency management and state management, simplifying infrastructure deployment and scaling."),

        (36, "Ansible", "Ansible is an open-source automation tool used for configuration management, application deployment, and task automation. It uses a simple, human-readable YAML syntax to define automation tasks and configurations. Ansible is agentless, meaning it does not require any special software to be installed on managed nodes. It is widely used for orchestrating complex workflows, managing infrastructure, and ensuring consistency across environments."),

        (37, "Jenkins", "Jenkins is an open-source automation server used for continuous integration and continuous delivery (CI/CD). It facilitates the automation of software build, test, and deployment processes, enabling developers to deliver code changes more frequently and reliably. Jenkins supports various plugins and integrations with version control systems, build tools, and deployment platforms, making it a central tool in DevOps practices."),

        (38, "AWS Lambda", "AWS Lambda is a serverless compute service provided by Amazon Web Services (AWS). It allows developers to run code in response to events without provisioning or managing servers. Lambda automatically scales the compute resources based on the incoming workload and charges only for the compute time consumed. It is commonly used for building event-driven applications, data processing, and microservices architecture."),

        (39, "Azure Functions", "Azure Functions is a serverless compute service offered by Microsoft Azure. It enables developers to run event-driven code without managing infrastructure. Azure Functions supports various triggers, such as HTTP requests, timers, and message queues, and provides built-in integrations with Azure services and external systems. It is used for automating tasks, processing data, and building scalable applications."),

        (40, "Google Cloud Functions", "Google Cloud Functions is a serverless execution environment provided by Google Cloud Platform. It allows developers to run code in response to events from Google Cloud services or external sources. Cloud Functions automatically scales based on demand and integrates with other Google Cloud services, such as Cloud Pub/Sub and Cloud Storage. It is used for building event-driven applications and microservices."),

        (41, "Blockchain", "Blockchain is a decentralized, distributed ledger technology that securely records transactions across a network of computers. Each block contains a list of transactions and is linked to the previous block, forming a chain. Blockchain provides transparency, immutability, and security, making it suitable for applications such as cryptocurrencies, supply chain management, and smart contracts."),

        (42, "Artificial Intelligence", "Artificial Intelligence (AI) refers to the simulation of human intelligence processes by machines, especially computer systems. AI encompasses various subfields, including machine learning, natural language processing, and computer vision. It is used to create systems that can perform tasks such as speech recognition, decision-making, and pattern recognition. AI is increasingly applied in areas like healthcare, finance, and autonomous vehicles."),

        (43, "Machine Learning", "Machine Learning (ML) is a subset of artificial intelligence that focuses on developing algorithms and statistical models that enable computers to learn from and make predictions or decisions based on data. ML techniques include supervised learning, unsupervised learning, and reinforcement learning. It is used in applications such as recommendation systems, fraud detection, and predictive analytics."),

        (44, "Deep Learning", "Deep Learning is a specialized subset of machine learning that involves neural networks with many layers, known as deep neural networks. It is used for tasks such as image and speech recognition, natural language processing, and autonomous driving. Deep learning models are trained on large datasets and can automatically extract features and patterns, achieving high performance in complex tasks."),

        (45, "Virtual Reality", "Virtual Reality (VR) is a technology that creates immersive, computer-generated environments that simulate real or imaginary worlds. VR typically requires a headset or goggles to provide a 360-degree view and interactive experience. It is used in various applications, including gaming, training simulations, education, and therapy, offering users a sense of presence and engagement in virtual environments."),

        (46, "Augmented Reality", "Augmented Reality (AR) overlays digital information onto the real world, enhancing the user's perception of their environment. AR is typically experienced through mobile devices, smart glasses, or AR headsets. It is used in applications such as navigation, interactive marketing, and remote assistance, blending digital content with the physical world to provide context and improve user experiences."),

        (47, "Internet of Things", "The Internet of Things (IoT) refers to the network of interconnected physical devices that collect and exchange data through the internet. IoT devices range from smart home appliances and wearable technology to industrial sensors and connected vehicles. IoT enables automation, remote monitoring, and data-driven insights, transforming various sectors such as smart cities, healthcare, and agriculture."),

        (48, "5G Technology", "5G technology represents the fifth generation of mobile network technology, offering significantly higher speeds, lower latency, and greater capacity compared to previous generations. It supports advanced applications such as enhanced mobile broadband, ultra-reliable low-latency communications, and massive machine-type communications. 5G is expected to drive innovations in areas like smart cities, autonomous vehicles, and immersive media."),

        (49, "Quantum Computing", "Quantum Computing is an emerging field that leverages the principles of quantum mechanics to perform computations that are infeasible for classical computers. Quantum computers use quantum bits or qubits to represent and process information in ways that can potentially solve complex problems faster than classical computers. Applications include cryptography, optimization, and simulations of quantum systems."),

        (50, "Edge Computing", "Edge Computing involves processing data closer to the source of generation, rather than relying on a centralized cloud or data center. It aims to reduce latency, improve response times, and alleviate bandwidth constraints by performing computations at the edge of the network. Edge computing is particularly useful for applications requiring real-time processing, such as IoT devices, autonomous systems, and remote monitoring.")

    ]

    for i, (id, name, description) in enumerate(file):
        img_data = open(img_paths[i], "rb").read()
        insert_query = '''INSERT INTO TechReviews (name, image, description) VALUES (?, ?, ?)'''
        record_data = (name, img_data, description)
        cursor.execute(insert_query, record_data)
        connection.commit()

except Error as e:
    print(f"Error: {e}")
finally:
    if connection:
        cursor.close()
        connection.close()