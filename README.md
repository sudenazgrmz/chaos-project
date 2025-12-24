
Kubernetes-based Alert Management System

 Project Overview
This repository demonstrates the application of Chaos Engineering principles on a Kubernetes-based microservice architecture using Chaos Mesh.
The goal of the project is to evaluate how a distributed system behaves under controlled failure scenarios such as:
* Network latency
* CPU resource exhaustion
* Pod termination
* HTTP-level request failures
The system simulates a simplified security alert processing pipeline, where incoming alerts are classified according to severity while chaos experiments are actively injected.
All experiments are documented with real execution screenshots, as required.

 Project Objectives
* Design a simple Kubernetes-based microservice system
* Apply controlled failures using Chaos Mesh CRDs
* Observe system behavior under different fault conditions
* Analyze fault tolerance, self-healing, and fallback mechanisms
* Document experiments with reproducible evidence (screenshots)

 System Architecture
Microservices
 Backend Service
* Exposes REST endpoint: /generate-alert
* Receives alert requests via HTTP
* Forwards alerts to the classifier
* Implements fallback logic if the classifier is unavailable
 Classifier Service
* Determines alert severity
* Runs as an independent Kubernetes Deployment
* Primary target of chaos experiments
 Client
* Manual testing via curl
* Used to observe system behavior during chaos
Communication Flow
Client → Backend → Classifier

 Technologies Used
* Kubernetes (Minikube)
* Docker
* Python (Flask)
* Chaos Mesh
* kubectl
* YAML-based manifests

 Chaos Engineering Experiments
All chaos experiments target the classifier service and are defined under the chaos-experiments/ directory. Each experiment is supported by execution screenshots stored under screenshots/.

 Experiment 1 – Baseline (No Chaos)
 screenshots/01_baseline/
Purpose: Establish normal system behavior before injecting chaos.
Evidence:
* Running pods
* Successful curl request
* Backend logs

 Experiment 2 – Network Delay (NetworkChaos)
 screenshots/02_network_delay/  network-delay-classifier.yaml  network-delay-backend-to-classifier.yaml
Description:
* Artificial latency injected between services
* Communication continues with increased delay
* No complete service outage observed
Observed Result:
* Backend successfully processes requests
* No timeout occurs under configured delay

 Experiment 3 – HTTP Chaos (HTTPChaos)
 screenshots/03_http_chaos/  http-chaos-classifier.yaml
Description:
* HTTP request aborts injected into classifier
* Experiment revealed runtime incompatibility between HTTPChaos and Docker-based container runtime
Observed Result:
* Chaos resource created successfully
* Injection failed due to container runtime mismatch
* Failure is documented and analyzed (expected technical limitation)
This experiment demonstrates important real-world constraints of chaos tooling.

 Experiment 4 – CPU Stress (StressChaos)
 screenshots/04_stress_chaos/  stress-cpu-classifier.yaml
Description:
* CPU load forced to 100% on classifier pod
* Service remains running but under heavy load
Observed Result:
* Curl requests still return responses
* Increased processing latency observed
* Demonstrates graceful degradation under resource pressure

 Experiment 5 – Pod Kill (PodChaos)
 screenshots/05_pod_kill/  pod-kill-classifier.yaml
Description:
* Classifier pod deliberately terminated
* Kubernetes automatically recreates the pod
Observed Result:
* Pod termination confirmed
* New pod created within seconds
* Demonstrates Kubernetes self-healing capability

 Experiment 6 – Composite Scenario (Pod Kill + Network Delay)
 screenshots/06_composite_scenario/
Description:
* Network delay and pod kill chaos active simultaneously
* Represents a realistic multi-failure incident scenario
Observed Result:
* NetworkChaos and PodChaos active at the same time
* Classifier pod recreated successfully
* System remains operational
Note: Due to limitations in the installed Chaos Mesh Workflow CRD, a native workflow experiment could not be applied. Instead, a manual composite chaos scenario was executed, which provides equivalent analytical value.

 Project Structure
chaos-mesh-demo/
│
├── chaos-experiments/
│   ├── http-chaos-classifier.yaml
│   ├── http-request-replacement-examples.yaml
│   ├── network-delay-backend-to-classifier.yaml
│   ├── network-delay-classifier.yaml
│   ├── pod-kill-classifier.yaml
│   └── stress-cpu-classifier.yaml
│
├── k8s/
│   ├── deployment.yaml
│   └── classifier-deployment.yaml
│
├── screenshots/
│   ├── 01_baseline/
│   ├── 02_network_delay/
│   ├── 03_http_chaos/
│   ├── 04_stress_chaos/
│   ├── 05_pod_kill/
│   └── 06_composite_scenario/
│
├── Dockerfile
├── requirements.txt
└── README.md

 Conclusion
This project successfully demonstrates how Chaos Engineering can be applied to a Kubernetes-based microservice system.
By injecting controlled failures using Chaos Mesh and documenting real execution results, the system’s resilience, recovery behavior, and limitations were analyzed in a practical and transparent manner.
The repository provides a reproducible, evidence-based chaos engineering study, aligned with academic and industry practices.


