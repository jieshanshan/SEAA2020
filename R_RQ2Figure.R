library(ggplot2)

p1 <- ggplot(RQ2confidence, aes(x=Type, y=Value)) +
  geom_boxplot(aes(fill=confidence), outlier.size = 2, outlier.shape = 1, fatten=1) +
  scale_x_discrete(breaks=c("Test, Doc", "Test, Code", "Test, Defect", "Documentation, Code", 
                            "Documentation, Defect", "Code, Defect", "Archi, Test", "Archi, Code", "Archi, Defect", "Archi, Doc"), 
                   labels=c("T,D", "T,C", "T,F", "D,C", 
                            "D,F", "C,F", "A,T", "A,C", "A,F", "A,D")) +
  scale_fill_manual(name = "co-occurrence", values = c("#6C7B95", "#C7F0DB"), labels = c(expression(a%->%b),expression(b%->%a)))+
  
  scale_y_continuous(breaks=c(0, 0.2, 0.4, 0.6, 0.8, 1.0),
                     labels=c(0, 0.2, 0.4, 0.6, 0.8, 1.0)) +
  labs(title="",x="Debt type (a,b)", y="Probability of co-occurrences", 
       caption = "")+  
  theme_light()+
  theme(panel.grid.minor.x = element_blank(),
        panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        axis.title.y = element_text(size = 12),
        axis.title.x = element_text(size = 12),
        axis.text.x = element_text(size = 12),
        axis.text.y = element_text(size = 12),
        legend.position="top",
        legend.text = element_text(size = 13),
        plot.margin = unit(c(-0.8,0.5,-0.4,0),"cm"))

p2 <- ggplot(RQ2support, aes(x=Type, y=Value)) +
  geom_boxplot(outlier.size = 2, outlier.shape = 1, width = 0.5, fatten=1) +
  scale_x_discrete(breaks=c("Test Debt", "Documentation Debt", "Code Debt", "Defect Debt","Architecture Debt"),
                   labels=c("T", "D", "C", "F", "A")) +
  scale_y_continuous(breaks=c(0, 0.2, 0.4, 0.6, 0.8, 1.0),
                     labels=c(0, 0.2, 0.4, 0.6, 0.8, 1.0)) +
  labs(title="",x="Debt type", y="Probability of debt types")  +
  theme_light()+
  theme(panel.grid.minor.x = element_blank(),
        panel.grid.major = element_blank(), 
        panel.grid.minor = element_blank(),
        axis.title.y = element_text(size = 12),
        axis.title.x = element_text(size = 12),
        axis.text.x = element_text(size = 12),
        axis.text.y = element_text(size = 12),
       # legend.position="top",
       # legend.text = element_text(size = 11),
        plot.margin = unit(c(0.55,0.5,0.15,0),"cm"))
#  theme(legend.position = "top")
  
p <-ggarrange(p1, p2, ncol=2, widths = c(7,3))

annotate_figure(p, bottom = text_grob("type (A=Architecture/Design Debt, C=Code Debt, F=Defect Debt, D=Documentation Debt, T=Test Debt)", size = 12)

)
  
  