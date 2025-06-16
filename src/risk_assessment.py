#!/usr/bin/env python3
"""
Third-Party Risk Assessment (TPRA) Tool
Author: Tebello
Description: Automated risk scoring and assessment for vendor evaluation
"""

import pandas as pd
import numpy as np
import json
import yaml
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Tuple, Any
import matplotlib.pyplot as plt
import seaborn as sns

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class VendorRiskAssessment:
    """Main class for conducting vendor risk assessments"""
    
    def __init__(self, config_path: str = "configs/settings.yaml"):
        """Initialize the risk assessment tool with configuration"""
        self.config = self._load_config(config_path)
        self.risk_categories = self.config['risk_categories']
        self.scoring_matrix = self.config['scoring_matrix']
        self.risk_thresholds = self.config['risk_thresholds']
        
    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from YAML file"""
        try:
            with open(config_path, 'r') as file:
                config = yaml.safe_load(file)
            logger.info(f"Configuration loaded from {config_path}")
            return config
        except FileNotFoundError:
            logger.error(f"Configuration file not found: {config_path}")
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict:
        """Return default configuration if config file is not found"""
        return {
            'risk_categories': {
                'security_controls': 0.25,
                'compliance': 0.20,
                'data_governance': 0.20,
                'business_continuity': 0.15,
                'operational_security': 0.10,
                'contract_legal': 0.10
            },
            'scoring_matrix': {
                'critical': 4,
                'high': 3,
                'medium': 2,
                'low': 1
            },
            'risk_thresholds': {
                'low': 85,
                'medium': 70,
                'high': 55,
                'critical': 0
            }
        }
    
    def load_vendor_data(self, data_path: str) -> pd.DataFrame:
        """Load vendor assessment data from CSV file"""
        try:
            df = pd.read_csv(data_path)
            logger.info(f"Vendor data loaded: {len(df)} vendors")
            return df
        except FileNotFoundError:
            logger.error(f"Vendor data file not found: {data_path}")
            return pd.DataFrame()
    
    def calculate_category_score(self, responses: Dict, category: str) -> float:
        """Calculate risk score for a specific category"""
        category_questions = self._get_category_questions(category)
        total_possible = len(category_questions) * self.scoring_matrix['critical']
        actual_score = 0
        
        for question in category_questions:
            if question in responses:
                actual_score += self._map_response_to_score(responses[question])
        
        # Convert to percentage
        percentage_score = (actual_score / total_possible) * 100 if total_possible > 0 else 0
        return round(percentage_score, 2)
    
    def _get_category_questions(self, category: str) -> List[str]:
        """Get list of questions for a specific risk category"""
        # This would typically be loaded from a configuration file
        # For demo purposes, using predefined question mappings
        question_mapping = {
            'security_controls': [
                'data_encryption_at_rest', 'data_encryption_in_transit', 'mfa_enforced',
                'rbac_implemented', 'vulnerability_scanning', 'patch_management',
                'incident_response_plan', 'security_team_dedicated'
            ],
            'compliance': [
                'soc2_certified', 'iso27001_certified', 'pci_compliant', 'gdpr_compliant',
                'hipaa_compliant', 'regular_audits', 'penetration_testing'
            ],
            'data_governance': [
                'data_retention_policy', 'data_deletion_procedures', 'data_portability',
                'cross_border_safeguards', 'privacy_impact_assessments', 'data_subject_rights'
            ],
            'business_continuity': [
                'uptime_sla', 'redundant_systems', 'geographic_distribution',
                'backup_procedures', 'disaster_recovery_plan', 'vendor_stability'
            ],
            'operational_security': [
                'background_checks', 'security_training', 'physical_security',
                'secure_disposal', 'insider_threat_monitoring'
            ],
            'contract_legal': [
                'comprehensive_sla', 'dpa_executed', 'liability_clauses',
                'termination_procedures', 'legal_jurisdiction', 'ip_protection'
            ]
        }
        return question_mapping.get(category, [])
    
    def _map_response_to_score(self, response: Any) -> int:
        """Map vendor response to risk score"""
        if isinstance(response, str):
            response = response.lower().strip()
            if response in ['yes', 'true', '1', 'compliant', 'implemented']:
                return self.scoring_matrix['critical']  # Best score
            elif response in ['partial', 'limited', 'in-progress']:
                return self.scoring_matrix['medium']
            elif response in ['no', 'false', '0', 'non-compliant', 'not-implemented']:
                return self.scoring_matrix['low']  # Worst score
        elif isinstance(response, (int, float)):
            if response >= 90:
                return self.scoring_matrix['critical']
            elif response >= 70:
                return self.scoring_matrix['high']
            elif response >= 50:
                return self.scoring_matrix['medium']
            else:
                return self.scoring_matrix['low']
        
        return self.scoring_matrix['low']  # Default to lowest score
    
    def calculate_overall_risk_score(self, vendor_data: Dict) -> Tuple[float, str]:
        """Calculate overall weighted risk score for a vendor"""
        weighted_score = 0
        category_scores = {}
        
        for category, weight in self.risk_categories.items():
            category_score = self.calculate_category_score(vendor_data, category)
            category_scores[category] = category_score
            weighted_score += category_score * weight
        
        # Determine risk level
        risk_level = self._determine_risk_level(weighted_score)
        
        return round(weighted_score, 2), risk_level, category_scores
    
    def _determine_risk_level(self, score: float) -> str:
        """Determine risk level based on score"""
        if score >= self.risk_thresholds['low']:
            return 'Low'
        elif score >= self.risk_thresholds['medium']:
            return 'Medium'
        elif score >= self.risk_thresholds['high']:
            return 'High'
        else:
            return 'Critical'
    
    def assess_vendor(self, vendor_name: str, vendor_data: Dict) -> Dict:
        """Conduct complete risk assessment for a single vendor"""
        logger.info(f"Assessing vendor: {vendor_name}")
        
        overall_score, risk_level, category_scores = self.calculate_overall_risk_score(vendor_data)
        
        assessment_result = {
            'vendor_name': vendor_name,
            'assessment_date': datetime.now().strftime('%Y-%m-%d'),
            'overall_score': overall_score,
            'risk_level': risk_level,
            'category_scores': category_scores,
            'recommendations': self._generate_recommendations(category_scores, risk_level),
            'next_assessment_date': self._calculate_next_assessment_date(risk_level)
        }
        
        return assessment_result
    
    def _generate_recommendations(self, category_scores: Dict, risk_level: str) -> List[str]:
        """Generate recommendations based on assessment results"""
        recommendations = []
        
        # Check each category for improvement opportunities
        for category, score in category_scores.items():
            if score < self.risk_thresholds['medium']:
                recommendations.append(f"Immediate attention required for {category.replace('_', ' ').title()}")
            elif score < self.risk_thresholds['low']:
                recommendations.append(f"Monitor and improve {category.replace('_', ' ').title()}")
        
        # Add general recommendations based on risk level
        if risk_level == 'Critical':
            recommendations.append("Consider alternative vendors or require immediate remediation")
        elif risk_level == 'High':
            recommendations.append("Develop detailed risk mitigation plan before engagement")
        elif risk_level == 'Medium':
            recommendations.append("Implement additional monitoring and controls")
        
        return recommendations if recommendations else ["Vendor meets acceptable risk standards"]
    
    def _calculate_next_assessment_date(self, risk_level: str) -> str:
        """Calculate next assessment date based on risk level"""
        base_date = datetime.now()
        
        if risk_level == 'Critical':
            next_date = base_date + timedelta(days=30)  # Monthly
        elif risk_level == 'High':
            next_date = base_date + timedelta(days=90)  # Quarterly
        elif risk_level == 'Medium':
            next_date = base_date + timedelta(days=180)  # Semi-annually
        else:  # Low risk
            next_date = base_date + timedelta(days=365)  # Annually
        
        return next_date.strftime('%Y-%m-%d')
    
    def batch_assess_vendors(self, vendor_df: pd.DataFrame) -> List[Dict]:
        """Conduct risk assessments for multiple vendors"""
        results = []
        
        for _, row in vendor_df.iterrows():
            vendor_name = row.get('vendor_name', 'Unknown')
            vendor_data = row.to_dict()
            
            try:
                assessment = self.assess_vendor(vendor_name, vendor_data)
                results.append(assessment)
            except Exception as e:
                logger.error(f"Error assessing {vendor_name}: {str(e)}")
                continue
        
        logger.info(f"Completed assessments for {len(results)} vendors")
        return results
    
    def save_assessment_results(self, results: List[Dict], output_path: str):
        """Save assessment results to JSON file"""
        try:
            with open(output_path, 'w') as file:
                json.dump(results, file, indent=2, default=str)
            logger.info(f"Assessment results saved to {output_path}")
        except Exception as e:
            logger.error(f"Error saving results: {str(e)}")
    
    def generate_summary_report(self, results: List[Dict]) -> Dict:
        """Generate summary statistics from assessment results"""
        if not results:
            return {}
        
        risk_levels = [r['risk_level'] for r in results]
        scores = [r['overall_score'] for r in results]
        
        summary = {
            'total_vendors_assessed': len(results),
            'risk_distribution': {
                'Critical': risk_levels.count('Critical'),
                'High': risk_levels.count('High'),
                'Medium': risk_levels.count('Medium'),
                'Low': risk_levels.count('Low')
            },
            'average_risk_score': round(np.mean(scores), 2),
            'median_risk_score': round(np.median(scores), 2),
            'highest_risk_vendors': [
                {'name': r['vendor_name'], 'score': r['overall_score'], 'level': r['risk_level']}
                for r in sorted(results, key=lambda x: x['overall_score'])[:5]
            ],
            'assessment_date': datetime.now().strftime('%Y-%m-%d')
        }
        
        return summary

def main():
    """Main execution function"""
    # Initialize risk assessment tool
    tpra = VendorRiskAssessment()
    
    # Load vendor data
    vendor_data = tpra.load_vendor_data('data/vendors_sample.csv')
    
    if vendor_data.empty:
        logger.error("No vendor data available for assessment")
        return
    
    # Conduct batch assessments
    assessment_results = tpra.batch_assess_vendors(vendor_data)
    
    # Save results
    tpra.save_assessment_results(assessment_results, 'data/risk_scores.json')
    
    # Generate summary report
    summary = tpra.generate_summary_report(assessment_results)
    
    # Print summary
    print("\n" + "="*50)
    print("THIRD-PARTY RISK ASSESSMENT SUMMARY")
    print("="*50)
    print(f"Total Vendors Assessed: {summary['total_vendors_assessed']}")
    print(f"Average Risk Score: {summary['average_risk_score']}%")
    print("\nRisk Distribution:")
    for level, count in summary['risk_distribution'].items():
        print(f"  {level}: {count} vendors")
    
    print("\nHighest Risk Vendors:")
    for vendor in summary['highest_risk_vendors']:
        print(f"  {vendor['name']}: {vendor['score']}% ({vendor['level']} Risk)")
    
    print(f"\nDetailed results saved to: data/risk_scores.json")
    print("="*50)

if __name__ == "__main__":
    main()