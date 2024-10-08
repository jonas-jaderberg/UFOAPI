/*
 * DATEX II Snapshot Pull API
 *
 * This is DATEX II Snapshot PULL API returning PayloadPublication.
 *
 * The version of the OpenAPI document: 1.0.2
 * Contact: you@your-company.com
 * Generated by: https://openapi-generator.tech
 */

using System;
using System.Linq;
using System.Text;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Org.OpenAPITools.Converters;

namespace Org.OpenAPITools.Models
{ 
    /// <summary>
    /// 
    /// </summary>
    [DataContract]
    public partial class GroupOfPeopleInvolved : IEquatable<GroupOfPeopleInvolved>
    {
        /// <summary>
        /// Gets or Sets NumberOfPeople
        /// </summary>
        [DataMember(Name="numberOfPeople", EmitDefaultValue=true)]
        public int NumberOfPeople { get; set; }

        /// <summary>
        /// Gets or Sets InjuryStatusType
        /// </summary>
        [DataMember(Name="injuryStatusType", EmitDefaultValue=false)]
        public InjuryStatusTypeEnumG InjuryStatusType { get; set; }

        /// <summary>
        /// Gets or Sets InvolvementRole
        /// </summary>
        [DataMember(Name="involvementRole", EmitDefaultValue=false)]
        public InvolvementRolesEnumG InvolvementRole { get; set; }

        /// <summary>
        /// Gets or Sets CategoryOfPeopleInvolved
        /// </summary>
        [DataMember(Name="categoryOfPeopleInvolved", EmitDefaultValue=false)]
        public PersonCategoryEnumG CategoryOfPeopleInvolved { get; set; }

        /// <summary>
        /// Gets or Sets GroupOfPeopleInvolvedExtensionG
        /// </summary>
        [DataMember(Name="groupOfPeopleInvolvedExtensionG", EmitDefaultValue=false)]
        public Dictionary<string, Object> GroupOfPeopleInvolvedExtensionG { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class GroupOfPeopleInvolved {\n");
            sb.Append("  NumberOfPeople: ").Append(NumberOfPeople).Append("\n");
            sb.Append("  InjuryStatusType: ").Append(InjuryStatusType).Append("\n");
            sb.Append("  InvolvementRole: ").Append(InvolvementRole).Append("\n");
            sb.Append("  CategoryOfPeopleInvolved: ").Append(CategoryOfPeopleInvolved).Append("\n");
            sb.Append("  GroupOfPeopleInvolvedExtensionG: ").Append(GroupOfPeopleInvolvedExtensionG).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="obj">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object obj)
        {
            if (obj is null) return false;
            if (ReferenceEquals(this, obj)) return true;
            return obj.GetType() == GetType() && Equals((GroupOfPeopleInvolved)obj);
        }

        /// <summary>
        /// Returns true if GroupOfPeopleInvolved instances are equal
        /// </summary>
        /// <param name="other">Instance of GroupOfPeopleInvolved to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(GroupOfPeopleInvolved other)
        {
            if (other is null) return false;
            if (ReferenceEquals(this, other)) return true;

            return 
                (
                    NumberOfPeople == other.NumberOfPeople ||
                    
                    NumberOfPeople.Equals(other.NumberOfPeople)
                ) && 
                (
                    InjuryStatusType == other.InjuryStatusType ||
                    InjuryStatusType != null &&
                    InjuryStatusType.Equals(other.InjuryStatusType)
                ) && 
                (
                    InvolvementRole == other.InvolvementRole ||
                    InvolvementRole != null &&
                    InvolvementRole.Equals(other.InvolvementRole)
                ) && 
                (
                    CategoryOfPeopleInvolved == other.CategoryOfPeopleInvolved ||
                    CategoryOfPeopleInvolved != null &&
                    CategoryOfPeopleInvolved.Equals(other.CategoryOfPeopleInvolved)
                ) && 
                (
                    GroupOfPeopleInvolvedExtensionG == other.GroupOfPeopleInvolvedExtensionG ||
                    GroupOfPeopleInvolvedExtensionG != null &&
                    other.GroupOfPeopleInvolvedExtensionG != null &&
                    GroupOfPeopleInvolvedExtensionG.SequenceEqual(other.GroupOfPeopleInvolvedExtensionG)
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                var hashCode = 41;
                // Suitable nullity checks etc, of course :)
                    
                    hashCode = hashCode * 59 + NumberOfPeople.GetHashCode();
                    if (InjuryStatusType != null)
                    hashCode = hashCode * 59 + InjuryStatusType.GetHashCode();
                    if (InvolvementRole != null)
                    hashCode = hashCode * 59 + InvolvementRole.GetHashCode();
                    if (CategoryOfPeopleInvolved != null)
                    hashCode = hashCode * 59 + CategoryOfPeopleInvolved.GetHashCode();
                    if (GroupOfPeopleInvolvedExtensionG != null)
                    hashCode = hashCode * 59 + GroupOfPeopleInvolvedExtensionG.GetHashCode();
                return hashCode;
            }
        }

        #region Operators
        #pragma warning disable 1591

        public static bool operator ==(GroupOfPeopleInvolved left, GroupOfPeopleInvolved right)
        {
            return Equals(left, right);
        }

        public static bool operator !=(GroupOfPeopleInvolved left, GroupOfPeopleInvolved right)
        {
            return !Equals(left, right);
        }

        #pragma warning restore 1591
        #endregion Operators
    }
}
