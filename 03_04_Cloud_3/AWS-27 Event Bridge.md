# Event Bridge
Amazon EventBridge is a serverless event bus that makes it easier to build event-driven applications at scale using events generated from your applications, integrated Software-as-a-Service (SaaS) applications, and AWS services.
## Key-terms
- Event Bus : An event bus is a pipeline that receives events. Rules associated with the event bus evaluate events as they arrive. Each rule checks whether an event matches the rule's criteria. You associate a rule with a specific event bus, so the rule only applies to events received by that event bus.
- Event : An event indicates a change in an environment such as an AWS environment, a SaaS partner service or application, or one of your applications or services.
- Rules : A rule matches incoming events and sends them to targets for processing. A single rule can send an event to multiple targets, which then run in parallel. Rules are based either on an event pattern or a schedule.
- Target : A target is a resource or endpoint that EventBridge sends an event to when the event matches the event pattern defined for a rule. The rule processes the event data and sends the pertinent information to the target. To deliver event data to a target, EventBridge needs permission to access the target resource. You can define up to five targets for each rule.
## Opdracht
### Gebruikte bronnen
- https://docs.aws.amazon.com/eventbridge/latest/userguide/



### Ervaren problemen

### Resultaat
